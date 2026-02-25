# Deploy Deep Agent to Railway

**If you see "We've paused free/trial deploys"** — Railway may be limiting free/trial accounts. Set variables in the **Dashboard** (Option A below), add a payment method or upgrade if required, and retry `railway up` later.

## 1. Get a valid Railway token

- **For `railway link` / `railway init`** (first-time setup): use an **account** token.  
  Go to **Personal → Tokens** → **New Token** → Create. **Copy the token immediately** — Railway shows the full value only once. Put it in `.env` as `RAILWAY_API_TOKEN` (or use `railway login` in a terminal and log in in the browser).

- **For `railway up`** (deploy): use a **project** token.  
  Create a project in the Railway dashboard, then **Project → Settings → Tokens → Generate**. Copy it once and set as `RAILWAY_TOKEN` when running the deploy command.

If you took the token from the **Tokens table** (where it shows `****-15b0`), that is only a masked value — you cannot use it. Create a **new** token and copy the full string when it is first shown.

## 2. Set env vars on Railway

**Required** (from your `week-4/.env`):

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key |
| `TAVILY_API_KEY` | Tavily search API key |

**Optional** (LangSmith observability):

| Variable | Value |
|----------|--------|
| `LANGCHAIN_TRACING_V2` | `true` |
| `LANGCHAIN_API_KEY` | Your LangSmith API key |
| `LANGCHAIN_PROJECT` | `deep-agent-demo` |

**Option A — Dashboard**  
Railway Dashboard → your project → **Variables** → Add each variable (paste values from `.env`).

**Option B — CLI from .env**  
From `backend/` with `RAILWAY_API_TOKEN` in `../.env`:

```bash
cd multi-agent-systems/week-4/backend
source ../.env 2>/dev/null || set -a && . ../.env && set +a
railway variables set OPENAI_API_KEY="$OPENAI_API_KEY" TAVILY_API_KEY="$TAVILY_API_KEY" \
  LANGCHAIN_TRACING_V2=true LANGCHAIN_API_KEY="$LANGCHAIN_API_KEY" LANGCHAIN_PROJECT=deep-agent-demo
```

Or run the script: `./set_railway_env.sh` (see below).

## 3. Deploy from this directory

```bash
cd multi-agent-systems/week-4/backend

# First time only: link to an existing project (needs account token or railway login)
export RAILWAY_API_TOKEN=<your-account-token>   # from Personal → Tokens, new token
railway link
# Pick your project, or create one in the dashboard and paste its ID

# Deploy (use project token for CI, or use railway login for interactive)
export RAILWAY_TOKEN=<your-project-token>       # from Project → Settings → Tokens
railway up
```

Or after `railway login` (browser):

```bash
railway link
railway up
```

## 4. Get the URL

After deploy, run `railway domain` or open the project in the dashboard to get the public URL. Test:

```bash
curl -X POST https://YOUR-APP.up.railway.app/research \
  -H "Content-Type: application/json" \
  -d '{"question": "What is LangGraph?"}'
```
