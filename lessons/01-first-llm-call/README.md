# Lesson 01: First LLM API Call 

My first hands-on experiment with **Large Language Models (LLMs)** using Python and the Groq API, as part of my AI Engineering learning journey.

## 📌 Overview

In this lesson, I created a Python application that sends a message to an LLM using the Groq API and prints the model's generated response.

The goal was to understand how a Python application communicates with an LLM through an API.

## 🛠️ Tech Stack

- **Python 3.12** — Programming language
- **Groq API** — Access to LLM inference
- **Groq Python SDK** — Communicate with the API
- **python-dotenv** — Load environment variables from a `.env` file
- **uv** — Python project and dependency management
- **Visual Studio Code** — Development environment

## 📚 Concepts Learned

- What an LLM API call is
- How to initialize a Groq client
- How to securely load an API key using environment variables
- How to specify a model
- How to structure messages using `role` and `content`
- How to send requests using `client.chat.completions.create()`
- How to extract and display the model's generated response
- Why a Python virtual environment is useful for project isolation

## 📂 Project Structure

```text
LLM_call_Practice/
├── .venv/          # Local virtual environment (not committed)
├── .env            # API key (not committed)
├── .gitignore      # Excludes secrets and local files
├── hello_llm.py    # First LLM API call
├── pyproject.toml  # Project configuration and dependencies
└── uv.lock         # Locked dependency versions
```

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LLM_call_Practice.git
cd LLM_call_Practice
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Install uv

If `uv` is not already installed, follow the official installation instructions:

https://docs.astral.sh/uv/getting-started/installation/

### 3. Create and activate the virtual environment

On Windows PowerShell:

```powershell
uv venv --python 3.12
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
uv sync
```

This installs the dependencies declared in `pyproject.toml` and resolved in `uv.lock`.

Alternatively, for a new project before its dependency configuration is committed:

```powershell
uv add groq python-dotenv
```

### 5. Configure the API key

Create a `.env` file in the project root:

```dotenv
GROQ_API_KEY=your_actual_groq_api_key
```

Get an API key from the Groq Console:

https://console.groq.com/keys

Replace the placeholder with your own key.

**Security note:** Never commit your `.env` file or expose your API key in public repositories.

## 💻 Implementation

The application uses the Groq SDK to send a user message to a language model and display its response.


The selected model must be available to your Groq API account. Model availability can change over time.

## ▶️ Run the Application

From the project directory, execute:

```powershell
python hello_llm.py
```

If VS Code is not using the correct interpreter, run the script explicitly with the project's virtual environment:

```powershell
.\.venv\Scripts\python.exe .\hello_llm.py
```

The model's response should appear in the terminal.

## 🔄 How the LLM Call Works

1. **Load configuration:** Read the API key from `.env`.
2. **Initialize the client:** Create a Groq client using the API key.
3. **Choose a model:** Specify the model identifier.
4. **Prepare messages:** Provide the conversation as a list of role/content objects.
5. **Send the request:** Call the chat completions API.
6. **Receive the response:** The API returns a completion object.
7. **Extract the text:** Read `response.choices[0].message.content`.

## 🔐 Security and Best Practices

The `.gitignore` file excludes local files and secrets:

```gitignore
.venv/
.env
__pycache__/
*.py[cod]
.ipynb_checkpoints/
```

Other practices:

- Keep API keys outside source code.
- Never commit secrets to GitHub.
- Use a virtual environment for each project.
- Handle missing environment variables explicitly.
- Verify that the selected model is supported by the provider.

## 🎯 Outcome

Successfully completed my first LLM API integration using Python and Groq.

This lesson established the foundation for learning system messages, temperature, prompt engineering, structured outputs, and more advanced AI application development.


---

**Part of my AI Engineering learning journey.** Learning by building, experimenting, debugging, and understanding how things work under the hood.
