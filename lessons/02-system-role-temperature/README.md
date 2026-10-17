# Lesson 02: System Role and Temperature

**Status:** Completed / continue experimenting

## Goal

Explore how system instructions shape the assistant’s behavior and how temperature can affect response variability when supported by the selected model.

## Learning objectives

By the end of this lesson, I should be able to:

- **System role:** Give the model a purpose, tone, boundaries, and task instructions.
- **User role:** Provide the actual question or request being handled.
- **Temperature:** Experiment with low and higher values only when the selected model/API supports the parameter.
- **Controlled comparison:** Keep the user prompt unchanged while changing one setting at a time; compare multiple runs instead of drawing conclusions from one response.

## Prerequisites

- Python basics: variables, functions, lists, dictionaries, and exceptions.
- A working project environment managed with `uv`.
- For lessons that call an LLM API, a valid provider API key configured locally in the root `.env` file.

## Project file

The planned/primary script for this lesson is `role_temp.py`.

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
python role_temp.py
```

If the script has not been created yet, treat this as the intended run command for when the lesson is implemented.

## Expected result

Run the same prompt with different system instructions and supported temperature values; record how the outputs differ. Temperature does not guarantee factuality or quality.

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
