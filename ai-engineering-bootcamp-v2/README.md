# AI Engineering Bootcamp v2

Hands-on course materials for building production-style LLM APIs with **FastAPI**, **OpenAI**, **Pydantic**, and **Streamlit**.

## Weeks

| Week | Topic | Location |
|------|-------|----------|
| 1 | `/ask` endpoint — typed I/O, structured output, guardrails, model selection, cost | [`week-1/`](week-1/) |

## Tech stack

- **FastAPI** — HTTP API with automatic OpenAPI docs
- **OpenAI Python SDK** — chat completions and structured output (`response_format`)
- **Pydantic** — request/response schemas and validation guardrails
- **python-dotenv** — load `OPENAI_API_KEY` from `.env`
- **Streamlit** — interactive demo runner (`demo_page.py`)
- **httpx** — HTTP client for tests and the Streamlit UI

## Quick start

```bash
cd week-1
cp .env.example .env          # add your OPENAI_API_KEY
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

See [week-1/README.md](week-1/README.md) for running each demo stage.
