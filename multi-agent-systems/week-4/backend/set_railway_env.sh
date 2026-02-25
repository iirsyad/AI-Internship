#!/usr/bin/env bash
# Set Railway env vars from week-4/.env (run from backend/ with RAILWAY_API_TOKEN in ../.env)
set -e
cd "$(dirname "$0")"
if [[ ! -f ../.env ]]; then
  echo "Missing ../.env. Create week-4/.env with OPENAI_API_KEY, TAVILY_API_KEY, LANGCHAIN_*."
  exit 1
fi
set -a
. ../.env
set +a
railway variables set \
  OPENAI_API_KEY="$OPENAI_API_KEY" \
  TAVILY_API_KEY="$TAVILY_API_KEY" \
  LANGCHAIN_TRACING_V2="${LANGCHAIN_TRACING_V2:-true}" \
  LANGCHAIN_API_KEY="${LANGCHAIN_API_KEY:-}" \
  LANGCHAIN_PROJECT="${LANGCHAIN_PROJECT:-deep-agent-demo}"
echo "Railway variables set."
