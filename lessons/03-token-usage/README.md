# Lesson 03: Token Usage

**Status:** Completed / continue experimenting

## Goal

Measure input and output token usage returned by the Groq API and understand why token counts matter for latency, limits, and cost.

## Learning objectives

By the end of this lesson, I should be able to:

- **Prompt tokens:** Tokens counted for the input messages and related request content.
- **Completion tokens:** Tokens generated in the model response.
- **Total tokens:** Read `response.usage.total_tokens` when the provider returns usage information.
- **Loop placement:** Keep request creation and usage printing inside the `for` loop so each prompt triggers a separate request.

## Prerequisites

- Python basics: variables, functions, lists, dictionaries, and exceptions.
- A working project environment managed with `uv`.
- For lessons that call an LLM API, a valid provider API key configured locally in the root `.env` file.

## Project file

The planned/primary script for this lesson is `tokens.py`.

## Setup

Run commands from the repository root. Install new dependencies only when the lesson needs them and keep the root `pyproject.toml` and `uv.lock` synchronized.

```powershell
uv sync
```

For example, add the dependency when instructed by the lesson:

```powershell
uv add pydantic
```

Do not copy `.env`, `.venv`, or API keys into lesson folders or commit them to GitHub.

## Run

```powershell
python tokens.py
```

If the script has not been created yet, treat this as the intended run command for when the lesson is implemented.

## Expected result

Try a greeting, a short question, and a detailed request. Compare the reported input and output usage. Counts depend on the model, tokenizer, and exact messages.

## Practice tasks

1. Run the example and explain each important line in your own words.
2. Change one input or configuration value and observe the result.
3. Test an edge case, invalid input, or provider failure where applicable.
4. Update this README with a short note about what you learned and any limitations you observed.

## Key takeaways

Write 3–5 points here after completing the lesson. Prefer specific observations from your own run over generic definitions.

## References

- Python documentation: https://docs.python.org/3/
- `uv` documentation: https://docs.astral.sh/uv/
- Groq documentation: https://console.groq.com/docs/ (for Groq API lessons)
