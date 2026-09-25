# 🤖 Local AI Chatbot with Streamlit & Ollama

A simple local AI chatbot built with **Python**, **Streamlit**, and **Ollama**.

This project provides a browser-based chat interface for interacting with locally installed Large Language Models (LLMs) through Ollama. The application automatically detects available Ollama models and lets you select a model from the sidebar.

---

## 📌 Project Overview

**Local AI Chatbot with Streamlit & Ollama** is designed for local AI experimentation and development.

### What the application does

- Uses **Streamlit** for the web interface.
- Uses the **Ollama Python client** to communicate with Ollama.
- Connects to the local Ollama server at `http://127.0.0.1:11434`.
- Automatically detects installed Ollama models.
- Allows model selection from the sidebar.
- Maintains conversation history during the current Streamlit session.
- Streams AI responses as they are generated.
- Provides a **Clear Chat History** button.
- Displays Ollama connection and model errors in the interface.

---

## ✨ Features

### 🏠 Local AI

The chatbot is designed to work with an Ollama server running locally on your computer.

> **Note:** Actual network behavior depends on your Ollama configuration. If Ollama is configured to use a remote endpoint, requests may not remain on the local machine.

### 💬 Interactive Chat

The application uses Streamlit's chat components:

- `st.chat_message()` for user and assistant messages
- `st.chat_input()` for entering prompts
- `st.session_state` for conversation history

### ⚡ Streaming Responses

Responses are streamed from Ollama and displayed progressively in the chat interface.

### 🧠 Conversation History

Messages are stored in Streamlit session state:

```python
st.session_state.messages
```

The stored conversation is sent to Ollama with each new request so the model can use previous messages from the current session.

### 🔎 Automatic Model Detection

The app checks the local Ollama server for installed models and displays them in the sidebar.

You can switch between available models without changing the Python source code.

### ⭐ Default Model

The application prefers:

```text
gemma3:4b
```

when it is installed.

If `gemma3:4b` is not available, the application selects the first detected model.

If no models are detected, you can manually enter a model name.

### 🟢 Connection Status

The sidebar shows the Ollama connection status:

- ✅ Ollama connected
- ❌ Ollama connection failed

When a connection fails, the interface also displays the configured Ollama host and the returned error.

### 🗑️ Clear Chat History

Use the **Clear Chat History** button in the sidebar to remove all messages from the current session.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Main programming language |
| Streamlit | Web UI and chatbot interface |
| Ollama | Local LLM runtime |
| Ollama Python Client | Communication between Python and Ollama |
| uv | Python project and dependency management |
| NumPy | Project dependency defined in `pyproject.toml` |

---

## 📂 Project Structure

```text
hammad-ahmad-suja-hammad_chatbot/
├── README.md
├── app.py
├── pyproject.toml
├── requirements.txt
├── .python-version
└── src/
    └── hammad_chatbot/
        └── __init__.py
```

### File Description

| File | Description |
| --- | --- |
| `README.md` | Project documentation |
| `app.py` | Main Streamlit chatbot application |
| `pyproject.toml` | Python project configuration and dependencies |
| `requirements.txt` | Python packages required to run the application |
| `.python-version` | Project Python version |
| `src/hammad_chatbot/__init__.py` | Package entry point |

---

# 🚀 Installation & Setup

## 1. Install Python

This project is configured for **Python 3.14**.

Check your installed version:

```bash
python --version
```

On Windows, you can also check:

```bash
py -3.14 --version
```

---

## 2. Install Ollama

Download and install Ollama from:

[https://ollama.com/](https://ollama.com/)

Verify the installation:

```bash
ollama --version
```

---

## 3. Start Ollama

Make sure the Ollama application/server is running.

The application is configured to connect to:

```text
http://127.0.0.1:11434
```

---

## 4. Install an Ollama Model

The application prefers `gemma3:4b`.

Pull the model:

```bash
ollama pull gemma3:4b
```

Check installed models:

```bash
ollama list
```

You can also test the model directly:

```bash
ollama run gemma3:4b
```

---

# 🐍 Python Environment Setup

There are two supported approaches for setting up the Python environment.

## Option A: Using `venv`

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows PowerShell

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

---

## Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

Or install the main packages directly:

```bash
pip install streamlit ollama
```

---

# ⚡ Option B: Using `uv`

This repository includes `pyproject.toml` and `.python-version`, so it can also be managed with `uv`.

Synchronize the project environment:

```bash
uv sync
```

Run the Streamlit application:

```bash
uv run streamlit run app.py
```

---

# ▶️ Run the Application

After installing Python dependencies and making sure Ollama is running, start the Streamlit application.

### Using `pip`

```bash
streamlit run app.py
```

### Using `uv`

```bash
uv run streamlit run app.py
```

Streamlit will normally provide a local URL such as:

```text
http://localhost:8501
```

Open that URL in your browser.

---

# 🖥️ How to Use

### Step 1 — Start Ollama

Make sure the Ollama application/server is running.

### Step 2 — Start Streamlit

Run:

```bash
streamlit run app.py
```

### Step 3 — Check the Sidebar

Look for the Ollama connection status.

You should see something like:

```text
✅ Ollama connected
```

### Step 4 — Select a Model

Choose a model from:

```text
Select local model
```

### Step 5 — Start Chatting

Enter your question in:

```text
Ask your local AI anything...
```

Press **Enter** and wait for the streamed response.

---

# 🧩 How the Application Works

The application follows this basic flow:

```text
User
  ↓
Streamlit Chat Interface
  ↓
User Prompt
  ↓
st.session_state.messages
  ↓
Ollama Python Client
  ↓
Local Ollama Server
  ↓
Selected Local LLM
  ↓
Streaming Response
  ↓
Streamlit Chat Window
```

---

# 🔌 Ollama Connection

The application creates the Ollama client with:

```python
OLLAMA_HOST = "http://127.0.0.1:11434"

client = Client(host=OLLAMA_HOST)
```

This means the app expects an Ollama server to be accessible at:

```text
127.0.0.1:11434
```

If the server cannot be reached, the sidebar displays a connection error.

---

# 🔎 Model Detection

The application uses the `get_available_models()` function to retrieve installed models:

```python
response = client.list()
```

The app extracts model names and displays them in the sidebar.

The code also includes fallback handling for different Ollama Python API response formats.

---

# 💬 Message Format

User messages are stored in the format expected by Ollama:

```python
{
    "role": "user",
    "content": "Hello"
}
```

Assistant messages use:

```python
{
    "role": "assistant",
    "content": "Hello! How can I help you?"
}
```

The complete message history is sent to Ollama:

```python
stream = client.chat(
    model=selected_model,
    messages=st.session_state.messages,
    stream=True
)
```

---

# ⚡ Streaming Response

The application enables streaming with:

```python
stream=True
```

Each response chunk is appended to the complete response:

```python
full_response += content
```

The Streamlit placeholder is updated as new content arrives:

```python
response_placeholder.markdown(full_response)
```

This produces a real-time response effect in the interface.

---

# 🧹 Clearing the Chat

When the **Clear Chat History** button is clicked, the application resets the message list:

```python
st.session_state.messages = []
```

Then it reloads the Streamlit interface:

```python
st.rerun()
```

---

# 🐛 Troubleshooting

## ❌ Ollama Connection Failed

### Cause

Ollama may not be running.

### Fix

Start Ollama and check:

```bash
ollama list
```

Then restart Streamlit:

```bash
streamlit run app.py
```

---

## ❌ No Models Detected

Check installed models:

```bash
ollama list
```

If the list is empty, install a model:

```bash
ollama pull gemma3:4b
```

Refresh the Streamlit page afterward.

---

## ❌ Model Not Found

Test the model manually:

```bash
ollama run gemma3:4b
```

Use the exact model name shown by:

```bash
ollama list
```

For another model:

```bash
ollama run <your-model-name>
```

---

## ❌ `streamlit` Command Not Found

Install Streamlit:

```bash
pip install streamlit
```

You can also run Streamlit through Python:

```bash
python -m streamlit run app.py
```

Or with `uv`:

```bash
uv run streamlit run app.py
```

---

## ❌ Ollama Python Package Error

Upgrade the Ollama Python package:

```bash
pip install --upgrade ollama
```

With `uv`:

```bash
uv add ollama
```

---

## ❌ PowerShell Activation Is Blocked

Run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## ❌ Python Version Problems

The project is configured for Python 3.14.

Check your current version:

```bash
python --version
```

Windows:

```bash
py -3.14 --version
```

With `uv`:

```bash
uv run python --version
```

---

# 🧪 Test Ollama Separately

Before troubleshooting Streamlit, make sure Ollama itself works.

### List models

```bash
ollama list
```

### Run a model

```bash
ollama run gemma3:4b
```

If the model works correctly, start Streamlit:

```bash
streamlit run app.py
```

This helps identify whether the problem is with Ollama or the Streamlit application.

---

# 📦 Dependencies

The current `pyproject.toml` defines:

```text
numpy>=2.5.3
ollama>=0.6.2
streamlit>=1.64.0
```

The current `requirements.txt` contains:

```text
streamlit
ollama
```

---

# 🔐 Privacy & Local Use

This project is designed around local Ollama inference.

The application connects to:

```text
http://127.0.0.1:11434
```

No OpenAI API key is required for the basic Ollama workflow.

> **Important:** Privacy depends on your local setup and Ollama configuration. If you configure Ollama or related services to use remote endpoints, data may leave the local machine.

---

# 🔑 API Keys

The basic application does **not** require:

- OpenAI API keys
- Anthropic API keys
- Gemini API keys
- Other cloud AI API keys

You need:

- Python
- Streamlit
- Ollama
- At least one Ollama model

---

# 🎯 Use Cases

This project can be used for:

- Local AI experimentation
- Learning Streamlit
- Learning Python-to-Ollama integration
- Building local chatbot prototypes
- Testing different Ollama models
- Creating a foundation for AI assistants
- Experimenting with future RAG applications

---

# 🚀 Future Improvements

Possible future additions include:

- [ ] Custom system prompts
- [ ] Temperature and model parameter controls
- [ ] Chat export and import
- [ ] Persistent conversation storage
- [ ] File upload
- [ ] Document chat
- [ ] RAG (Retrieval-Augmented Generation)
- [ ] Vector database integration
- [ ] Multiple chat sessions
- [ ] Authentication
- [ ] Voice input and output
- [ ] Model performance statistics
- [ ] Token/response monitoring
- [ ] Custom themes
- [ ] Docker deployment

---

# 🏗️ Development

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd hammad-ahmad-suja-hammad_chatbot
```

Create the environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Pull the Ollama model:

```bash
ollama pull gemma3:4b
```

Run the application:

```bash
streamlit run app.py
```

---

# 📸 Screenshots

You can add screenshots to the repository like this:

```text
screenshots/
├── chatbot-home.png
├── model-selection.png
└── chat-response.png
```

Then display them in the README:

```markdown
![Chatbot Interface](screenshots/chatbot-home.png)
```

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test the application locally.
5. Commit your changes.
6. Push the branch.
7. Open a Pull Request.

Example:

```bash
git checkout -b feature/new-feature
```

Commit your changes:

```bash
git add .
git commit -m "Add new feature"
```

Push the branch:

```bash
git push origin feature/new-feature
```

---

# 📝 Commit Message Examples

```text
feat: add model selection
fix: handle Ollama connection errors
docs: improve README
refactor: simplify chat handling
style: update Streamlit UI
```

---

# 📄 License

No license is currently specified in the project files.

Before publishing the project for public reuse, add an appropriate open-source license if you want others to legally reuse, modify, or distribute the code.

Common choices include:

- [MIT License](https://choosealicense.com/licenses/mit/)
- [Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
- [GNU GPL v3](https://choosealicense.com/licenses/gpl-3.0/)

---

# 👨‍💻 Author

**Hammad Ahmad**

GitHub: `https://github.com/YOUR-GITHUB-USERNAME`

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

# 📌 Quick Start

If Python and Ollama are already installed:

```bash
ollama pull gemma3:4b
pip install -r requirements.txt
streamlit run app.py
```

Then open:

[http://localhost:8501](http://localhost:8501)

---

# 📬 Project Summary

**Local AI Chatbot with Streamlit & Ollama** combines:

```text
Python
  +
Streamlit
  +
Ollama
  +
Local LLM
```

to provide a simple browser-based conversational AI experience.

This repository can serve as a foundation for building more advanced local AI applications.
