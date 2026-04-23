# Agentic Day 1

A simple demo showing how to use the Google Gemini generative model with LangChain in Python.

## Project overview

This repository contains a small proof-of-concept script that demonstrates:
- loading environment variables with `python-dotenv`
- creating a `ChatGoogleGenerativeAI` instance
- making a naive stateless LLM call
- fixing context by using the LangChain `messages` API
- explaining the difference between string-based and message-based invocation

The current entrypoint is `app.py`.

## Requirements

Dependencies are listed in `requirments.txt`.

At minimum, this project needs:
- Python 3.12
- `langchain_google_genai`
- `python-dotenv`
- `langchain-core`

## Setup

From the project root:

```bash
cd /Users/vinod/Documents/Agentic-AI-Cohort/agentic-day1
```

### Using the existing environment

If you already have the included `env/` directory, activate it first:

```bash
source env/bin/activate
```

### Create a new virtual environment (optional)

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirments.txt
```

## Running the demo

```bash
python app.py
```

The script will print:
- a first response from a standalone invocation
- a second response that demonstrates stateless failure
- a third response using message history to preserve context

## What this project teaches

- LLM calls are stateless by default.
- Reusing conversation history is required to preserve context across turns.
- The LangChain `messages` API is the correct way to send structured chat history.

## Notes

- Ensure your `.env` file contains any required Google Gemini credentials before running the script.
- The code uses `gemini-2.5-flash-lite` as the model name.
- The reflection comments in `app.py` explain exactly why the first approach fails and why the second works.

## File structure

- `app.py` — demo script with context handling examples
- `requirments.txt` — dependency list
- `README.md` — project documentation
