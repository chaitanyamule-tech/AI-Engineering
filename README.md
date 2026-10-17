# AI Engineering Journey 🚀

A hands-on learning repository documenting my journey toward AI engineering through practical Python exercises, LLM integrations, prompt engineering, and progressively more advanced AI applications.

## Learning Roadmap

| Lesson | Topic | Practical Work |
|---|---|---|
| 01 | First LLM API Call | Connect Python to an LLM using the Groq API |
| 02 | System Role and Temperature | Experiment with model instructions and generation settings |
| 03 | Token Usage | Inspect prompt, completion, and total token usage |
| 04 | Prompt Engineering | Build a customer complaint classification workflow |
| 05 | JSON and Pydantic | Learn structured data, parsing, and validation |
| 06 | FastAPI for AI Applications | Expose an AI capability through an API |
| 07 | Structured LLM Outputs | Validate model responses against defined schemas |

## Tech Stack

- Python 3.12+
- Groq API and Python SDK
- `python-dotenv`
- `uv` for Python dependency management
- Pydantic and FastAPI as the learning roadmap progresses

## Repository Structure

Each lesson has its own folder containing the relevant source code and README. The root project configuration manages shared dependencies.

## Getting Started

Install `uv`, clone this repository, and synchronize the dependencies:

```powershell
git clone https://github.com/chaitanyamule-tech/AI-Engineering.git
cd AI-Engineering
uv sync
```

Create a local `.env` file containing your Groq API key. Never commit secrets.

Run a lesson from the repository root:

```powershell
uv run python lessons/01-first-llm-call/hello_llm.py
```

## Learning Philosophy

Learn by building, experimenting, debugging, documenting results, and understanding why the implementation works—not just by copying code.

This repository will evolve alongside my AI engineering learning journey.
