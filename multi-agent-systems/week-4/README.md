# Week 4: Evaluation, Monitoring & Shipping

## Making Your Agent Production-Ready

This week demonstrates how to make your AI systems production-ready with observability, evaluation, and monitoring using Langfuse.

## 🎯 What This Example Shows

A simple Research Assistant that demonstrates Langfuse features:

- **Tracing** - See every LLM call, tool use, and decision
- **Sessions** - Group traces by user session
- **Scores** - Track quality metrics (relevance, latency)
- **Multiple Spans** - Query analysis, generation, validation as separate traceable steps

## 🚀 Quick Start

### 1. Set Up API Keys

Create a `.env` file in the `backend/` directory:

```bash
OPENAI_API_KEY=your_openai_api_key_here
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=https://cloud.langfuse.com
```

Get your keys:
- **OpenAI**: https://platform.openai.com/api-keys
- **Langfuse**: https://cloud.langfuse.com (free tier available)

### 2. Run Locally

**Backend:**
```bash
cd backend
python -m uvicorn main:app --reload
```

**Frontend:**
```bash
cd frontend
streamlit run app.py
```

### 3. View in Langfuse Dashboard

After making a query, check your Langfuse dashboard to see:
- **Traces**: Full execution tree with multiple spans
- **Scores**: Relevance and latency metrics
- **Sessions**: All messages grouped by session ID

## 📁 Project Structure

```
week-4/
├── backend/
│   ├── main.py              # FastAPI app with Langfuse integration
│   ├── requirements.txt      # Dependencies
│   └── README.md            # Deployment guide
├── frontend/
│   ├── app.py               # Streamlit chat interface
│   └── requirements.txt     # Dependencies
└── README.md                # This file
```

## 🔍 Langfuse Features Demonstrated

### Tracing
Every function decorated with `@observe()` becomes a span in Langfuse:

```python
@observe()
def query_analysis(query: str) -> dict:
    """Creates a span: query_analysis"""
    
@observe()
def generate_response(query: str) -> str:
    """Creates a span: generate_response"""
    
@observe()
def validate_response(response: str) -> dict:
    """Creates a span: validate_response"""
```

The trace tree shows:
```
research_assistant (trace)
  ├── query_analysis (span)
  ├── generate_response (span)
  └── validate_response (span)
```

### Scoring
Scores are automatically logged to Langfuse:

- **relevance**: How well the response matches the query (0-1)
- **latency_ok**: Whether response time is under 3 seconds (0 or 1)

### Sessions & Users
- Sessions are tracked via `X-Session-ID` header
- Users are tracked via `X-User-ID` header
- All traces in a session are grouped together in Langfuse

## 📊 Viewing Traces in Langfuse

1. Go to your Langfuse dashboard: https://cloud.langfuse.com
2. Navigate to **Observability → Tracing**
3. Click on any trace to see:
   - Full trace tree with all spans
   - Input/output for each span
   - Token count and cost per span
   - Latency for each step
   - Scores attached to the trace

## 🚢 Deployment

See deployment guides:
- `backend/README.md` - Deploy backend to Render
- `frontend/README.md` - Deploy frontend to Streamlit Cloud
- `DEPLOYMENT_GUIDE.md` - Complete deployment guide

## 🎓 Learning Objectives

By the end of this week, you will:

- ✅ Understand how Langfuse provides observability for AI systems
- ✅ See how `@observe()` decorator creates automatic traces
- ✅ Learn how to add scores to traces
- ✅ Understand session and user tracking
- ✅ Deploy a production-ready AI system

## 🔗 Resources

- [Langfuse Documentation](https://langfuse.com/docs)
- [Langfuse Cloud](https://cloud.langfuse.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Streamlit Documentation](https://docs.streamlit.io)

## 💡 Key Takeaways

1. **Tracing is automatic** - Just add `@observe()` decorator
2. **Scores provide metrics** - Track what matters (relevance, latency, quality)
3. **Sessions group traces** - See full conversations, not just individual calls
4. **Simple is better** - Start with basic tracing, add complexity as needed

---

**Happy Building!** 🚀
