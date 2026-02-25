# AI Engineering Bootcamp - Week 4: Langfuse Observability

This folder contains a simple example demonstrating OpenAI integration with Langfuse observability.

## Overview

This example shows how to:
- Call OpenAI API with automatic tracing using Langfuse
- Load prompts from Langfuse Prompt Management
- Send traces to Langfuse dashboard for observability

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a `.env` file in this directory:

```bash
OPENAI_API_KEY=your_openai_api_key_here
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
LANGFUSE_HOST=https://cloud.langfuse.com
```

Get your keys:
- **OpenAI**: https://platform.openai.com/api-keys
- **Langfuse**: https://cloud.langfuse.com (free tier available)

### 3. Run the Script

```bash
python simple_openai_langfuse.py
```

## What the Script Does

1. **Initializes Langfuse client** - Connects to your Langfuse project
2. **Loads a prompt** - Fetches `research_assistant_system_prompt` from Langfuse Prompt Management
3. **Calls OpenAI** - Uses Langfuse's OpenAI wrapper for automatic tracing
4. **Sends trace** - Automatically sends the trace to Langfuse dashboard

## Key Features

### Automatic Tracing
Using `langfuse.openai` wrapper automatically traces all OpenAI API calls:
```python
from langfuse.openai import openai

result = openai.chat.completions.create(...)
```

### Prompt Management
Load prompts from Langfuse Prompt Management:
```python
prompt = langfuse.get_prompt("prompt-name")
prompt_text = prompt.prompt
model = prompt.config.get("model", "gpt-3.5-turbo")
```

### Trace Visibility
Traces appear in your Langfuse dashboard within 2-5 seconds after calling `langfuse.flush()`.

## View Traces

1. Go to your Langfuse dashboard: https://cloud.langfuse.com
2. Navigate to **Observability → Tracing**
3. Click on any trace to see:
   - Full request/response details
   - Token usage and costs
   - Latency metrics
   - Prompt information

## Files

- `simple_openai_langfuse.py` - Simple example script
- `requirements.txt` - Python dependencies

## Related Examples

For more advanced examples including FastAPI backend and Streamlit frontend, see:
- `ai-engineering-bootcamp/eval-monitoring-shipping/`

## Resources

- [Langfuse Documentation](https://langfuse.com/docs)
- [Langfuse Cloud](https://cloud.langfuse.com)
- [OpenAI API Documentation](https://platform.openai.com/docs)

