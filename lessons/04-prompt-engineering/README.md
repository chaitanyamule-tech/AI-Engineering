# Lesson 04: Prompt Engineering — Complaint Classification

**Status:** Completed / continue testing

## Goal

Build a text classifier that maps printing-kiosk complaints to BILLING, TECHNICAL, RETURN, or OTHER.

## Learning objectives

By the end of this lesson, I should be able to:

- **Clear task and labels:** Define each label and make categories mutually understandable.
- **Examples:** Provide representative examples, including edge cases.
- **Fallback:** Use OTHER when the complaint falls outside the supported categories.
- **Python formatting:** Use an f-string or another template mechanism to insert the actual complaint into the prompt.
- **Output constraints:** Ask for one label only, then validate the result in Python.

## Prerequisites

- Python basics: variables, functions, lists, dictionaries, and exceptions.
- A working project environment managed with `uv`.
- For lessons that call an LLM API, a valid provider API key configured locally in the root `.env` file.

## Project file

The planned/primary script for this lesson is `ai_prompt.py`.

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
python ai_prompt.py
```

If the script has not been created yet, treat this as the intended run command for when the lesson is implemented.

## Expected result

Test extra charges, failed printing, refund requests, and unrelated questions. A missing printout usually maps to TECHNICAL under the current label definitions.

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
