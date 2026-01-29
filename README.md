# Veronica

Veronica is a modular AI agent ecosystem designed to serve as a personal assistant and knowledge expert. This project integrates voice recording, retrieval-augmented generation (RAG), and the Model Context Protocol (MCP) to create a versatile AI capable of interacting with the world and providing specialized information.

## 🚀 Key Features

*   **Model Context Protocol (MCP) Server**: Exposes a standardized server (Veronica) capable of hosting tools for external integrations (currently structured for WhatsApp and Instagram notifications/messaging).
*   **Agentic RAG**: A specialized knowledge agent leveraging Vector Databases to answer domain-specific questions (demonstrated with a Thai Cuisine knowledge base).
*   **General Purpose Assistant**: A "Basic Agent" powered by Google Gemini and real-time web search (DuckDuckGo).
*   **Voice Capability**: Built-in modules for capturing high-quality audio, laying the groundwork for voice-to-voice interaction.

## 🛠️ Tech Stack

This project leverages a modern stack of AI and Python technologies:

### Core Frameworks
*   **[Agno](https://github.com/agno-agi/agno)**: The primary framework used for orchestrating AI agents, managing knowledge bases, and handling tool execution.
*   **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)**: Used via the `mcp` Python SDK to create a standardized server interface for AI tools.
*   **Google Gemini**: The underlying LLM power.
    *   **Gemini 2.0 Flash**: For high-speed text generation and reasoning.
    *   **Text Embedding 004**: For generating vector embeddings in the RAG pipeline.

### Data & Search
*   **[LanceDB](https://lancedb.com/)**: A serverless vector database used to store and retrieve knowledge embeddings for RAG.
*   **DuckDuckGo**: Integrated for real-time web search capabilities.

### Utilities & Systems
*   **PyAudio & Pydub**: For audio recording and processing.
*   **Python-Dotenv**: For secure environment variable management.

## 📦 Prerequisites

*   Python 3.10+
*   **Google API Key**: You will need an API key from [Google AI Studio](https://aistudio.google.com/) for Gemini models.
*   **PortAudio**: Required for `pyaudio`.
    *   *Windows*: Usually installs automatically with the pip package.
    *   *Mac*: `brew install portaudio`
    *   *Linux*: `sudo apt-get install python3-pyaudio`

## ⚙️ Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd veronica
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

## 🏃 Usage

The project contains several standalone modules for different functionalities:

### 1. Run the MCP Server
Start the Veronica server which exposes tools for handling data and notifications.
```bash
python server.py
```
*Note: By default, this runs on stdio transport, but can be configured for SSE.*

### 2. Run the Basic Agent
Launch the general-purpose assistant that can answer questions using web search.
```bash
python basic_agent.py
```

### 3. Run the RAG Agent (Thai Cuisine Expert)
Query the specialized agent that references a PDF knowledge base.
```bash
python agentic_rag.py
```

### 4. Record Audio
Test the microphone recording functionality (records for 5 seconds by default).
```bash
python Veronica.py
```

## 📂 Project Structure

*   `server.py`: The entry point for the FastMCP server, defining tools for social media and data fetching.
*   `basic_agent.py`: Implementation of a general agent using Agno + Gemini + DuckDuckGo.
*   `agentic_rag.py`: A RAG implementation using Agno + LanceDB, configured to learn from PDFs.
*   `record.py`: Core logic for audio recording and WAV file generation.
*   `Veronica.py`: A script demonstrating the usage of the recording module.
*   `requirements.txt`: Project dependencies.