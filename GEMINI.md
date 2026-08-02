# Project Overview
`personal-agent` is an AI-driven personal assistant built with LangChain, LangGraph, and FastAPI. It is designed to answer questions related to Prakashsinh Rajput's work experience, skills, and professional background by processing his resume.

# Project Type: Python Application (FastAPI + LangGraph)

# Directory Structure
- `app/`: Main application source code.
  - `agents/`: Contains LangGraph agent logic.
  - `tools/`: Utility functions, including resume parsing.
  - `main.py`: FastAPI entry point.
- `docs/`: Contains the source resume file (`Prakashsinh_Rajput_NodeJS.docx`).
- `pyproject.toml`: Project configuration and dependencies (managed by `uv`).

# Technologies
- **LangGraph**: For managing agent state and workflow.
- **LangChain**: For LLM integration (OpenAI).
- **FastAPI**: For exposing the agent via a REST API.
- **docx2txt**: For extracting text from Word documents.
- **uv**: For project initialization and dependency management.

# Building and Running

## Prerequisites
- [uv](https://github.com/astral-sh/uv) installed on your system.
- An OpenAI API Key.

## Setup
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Add your `OPENAI_API_KEY` to the `.env` file.

## Running the App
Use `uv` to run the FastAPI server:
```bash
uv run python app/main.py
```
The API will be available at `http://localhost:8000`.

## API Endpoints
- **GET /**: Health check.
- **POST /ask**: Query the agent.
  - Payload: `{"question": "What are your core skills?"}`

## Running with Docker
1. Build the image:
   ```bash
   docker build -t personal-agent .
   ```
2. Run the container (make sure to pass your API key):
   ```bash
   docker run -p 8000:8000 -e OPENAI_API_KEY="your_api_key" personal-agent
   ```

# Development Conventions
- Modular code structure: Keep agents and tools in separate directories.
- Use `uv` for all dependency management.
- Documentation-first approach.
