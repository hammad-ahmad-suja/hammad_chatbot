# Local AI Chatbot with Streamlit and Ollama

This project provides a simple, local web interface for interacting with LLMs running via [Ollama](https://ollama.com).

## 🚀 Getting Started

### 1. Install Ollama
Download and install Ollama from [ollama.com](https://ollama.com).

### 2. Pull the Model
Open your terminal (PowerShell or CMD) and download the Llama 3 model:
```bash
ollama pull llama3
```

### 3. Setup Python Environment
It is recommended to use a virtual environment:
```bash
# Create virtual environment
python -m venv .venv
# Activate it (Windows)
.\.venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Application
```bash
streamlit run app.py
```

## 🛠️ Features
- **Local Execution**: Your data never leaves your machine.
- **Streaming Responses**: Real-time text generation.
- **Session History**: Remembers previous parts of the conversation.
- **Model Selection**: Easily switch between models in the sidebar.

## 📦 Requirements
- Python 3.9+
- Ollama installed and running
- `llama3` model (or other models of your choice)
