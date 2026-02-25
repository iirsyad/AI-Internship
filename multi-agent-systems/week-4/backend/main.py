"""
Week 4: Deep Agent API — FastAPI + Deep Agents + LangSmith
Deploy to Railway with: railway up
"""

import os
import json
import time
from typing import Literal, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

load_dotenv()

os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
os.environ.setdefault("LANGCHAIN_PROJECT", "deep-agent-production")

from deepagents import create_deep_agent
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
):
    """Run a web search and return results with titles, URLs, and content snippets."""
    return tavily_client.search(query, max_results=max_results, topic=topic)


agent = create_deep_agent(
    model="openai:gpt-4.1",
    tools=[internet_search],
    system_prompt=(
        "You are an expert research assistant. Conduct thorough research "
        "and provide clear, well-structured answers. Be concise but comprehensive."
    ),
)

app = FastAPI(title="Deep Agent API — Week 4")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ResearchRequest(BaseModel):
    question: str


def _message_content_to_str(content) -> str:
    """Handle message content as string or list of blocks (e.g. [{'type': 'text', 'text': '...'}])."""
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                parts.append(block.get("text") or block.get("content") or "")
            else:
                parts.append(str(block))
        return " ".join(p for p in parts if p).strip() or ""
    return str(content)


class ResearchResponse(BaseModel):
    answer: str
    latency: float


@app.post("/research", response_model=ResearchResponse)
async def research(req: ResearchRequest):
    """Run the deep agent and return the full result."""
    start = time.time()
    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": req.question}]}
        )
        raw = result["messages"][-1].content
        answer = _message_content_to_str(raw)
        return ResearchResponse(answer=answer, latency=time.time() - start)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/research/stream")
async def research_stream(req: ResearchRequest):
    """Run the deep agent with streaming SSE output."""

    async def event_stream():
        try:
            async for event in agent.astream_events(
                {"messages": [{"role": "user", "content": req.question}]},
                version="v2",
            ):
                kind = event.get("event")
                if kind == "on_chat_model_stream":
                    chunk = event["data"].get("chunk")
                    if chunk and hasattr(chunk, "content") and chunk.content:
                        yield f"data: {json.dumps({'content': chunk.content})}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "deep-agent-api",
        "tracing": os.environ.get("LANGCHAIN_TRACING_V2", "false"),
        "project": os.environ.get("LANGCHAIN_PROJECT", "not set"),
    }


@app.get("/")
async def root():
    return {
        "service": "Deep Agent API — Week 4",
        "endpoints": {
            "POST /research": "Sync research (returns full answer)",
            "POST /research/stream": "Streaming research (SSE)",
            "GET /health": "Health check",
        },
    }


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
