# Codebase Companion: LLM-Powered Chatbot for GitHub Repositories 🤖

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://codebase-companion-9khggejvu36vgelmfezeah.streamlit.app/)

An intelligent chatbot that allows you to have a natural language conversation with any public GitHub repository. Powered by a Retrieval-Augmented Generation (RAG) pipeline, this tool helps developers quickly understand new codebases, find specific information, and accelerate their workflow.

## 🚀 Live Demo

[**Try Codebase Companion Now!**](https://codebase-companion-9khggejvu36vgelmfezeah.streamlit.app/)  <!-- 👈 **IMPORTANT: REPLACE THIS URL WITH YOUR LIVE STREAMLIT APP URL!** -->

## 📸 Screenshot

<!-- **IMPORTANT: ADD A SCREENSHOT OF YOUR APP IN ACTION HERE!** -->
<!-- You can drag and drop an image into the GitHub editor to upload it. -->
![App Screenshot]
<img width="1086" height="612" alt="image" src="https://github.com/user-attachments/assets/28250750-1586-45d7-bd53-a6ac489fdf5d" />


## ✨ Features

-   **Chat with Any Public Repository:** Simply provide a GitHub URL to start a conversation.
-   **Natural Language Q&A:** Ask questions about the project's purpose, architecture, specific functions, and more.
-   **Intelligent Contextual Answers:** Leverages the power of Google's Gemini 1.5 model and a RAG pipeline to provide context-aware responses based on the repository's actual code and documentation.
-   **Fast and Efficient:** Uses a local Hugging Face model for embeddings and a FAISS vector store for rapid, in-memory semantic search.
-   **Secure and Deployable:** API keys are managed securely using environment variables, and the entire application is deployed as a live web service.

## 🛠️ Tech Stack & Architecture

This project is an end-to-end AI application built with a modern, modular stack:

-   **AI & Machine Learning:**
    -   **LLM:** Google Gemini 1.5 Flash
    -   **Framework:** LangChain
    -   **Architecture:** Retrieval-Augmented Generation (RAG)
    -   **Embeddings:** Hugging Face `all-MiniLM-L6-v2` (Local & Open-Source)
    -   **Vector Store:** FAISS (Facebook AI Similarity Search)
-   **Backend:** Python
-   **Frontend:** Streamlit
-   **Cloud & DevOps:**
    -   **Hosting:** Streamlit Community Cloud
    -   **Version Control:** Git & GitHub
    -   **Dependency Management:** `requirements.txt` (Python), `packages.txt` (System)

### How It Works

1.  **Clone Repository:** The user provides a GitHub URL, which is cloned into a temporary folder on the server.
2.  **Load & Chunk:** The application loads all relevant text-based files (`.py`, `.md`, `.txt`, etc.) and splits them into smaller, manageable chunks.
3.  **Embed & Store:** Each chunk is converted into a numerical vector (embedding) using a local Hugging Face model. These embeddings are then stored in a high-speed FAISS vector database in memory.
4.  **User Query:** The user asks a question in the chat interface.
5.  **Semantic Search:** The user's question is also embedded, and FAISS performs a similarity search to find the most relevant text chunks from the codebase.
6.  **Generate Response:** The relevant chunks (context) and the original question are passed to the Gemini LLM, which generates a comprehensive, human-like answer.
7.  **Display:** The answer is displayed to the user in the Streamlit UI.

## ⚙️ Getting Started: Running Locally

To run this project on your own machine, follow these steps.

### Prerequisites

-   [Git](https://git-scm.com/downloads)
-   [Python 3.9+](https://www.python.org/downloads/)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

Install all the required Python packages.

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

This project requires a Google API key to use the Gemini model.

1.  Create a file named `.env` in the root of the project directory.
2.  Inside the `.env` file, add your Google API key in the following format:

    ```
    GOOGLE_API_KEY="AIzaSy...your...secret...api...key"
    ```
    > **Note:** Your `.env` file is listed in `.gitignore` and will never be committed to the repository.

### 4. Run the Streamlit App

Start the application by running:

```bash
streamlit run app.py
```

A new tab should open in your browser at `http://localhost:8501`.

## ☁️ Deployment

This application is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud). The deployment relies on two key files:
-   `requirements.txt`: For all Python package dependencies.
-   `packages.txt`: To install system-level dependencies like `git` on the cloud server.

Secrets (like the `GOOGLE_API_KEY`) are managed securely using Streamlit's built-in secret management.

## 🚀 Future Improvements

-   [ ] **Chat History:** Implement a session state to store and display the conversation history.
-   [ ] **Show Sources:** Display the specific file names and text chunks that were used as context for generating an answer.
-   [ ] **Support for Private Repositories:** Add authentication to allow users to connect their GitHub accounts and chat with private codebases.
-   [ ] **Improved Error Handling:** Add more robust error handling for invalid URLs and repository cloning failures.

---

*Built by [Your Name](https://github.com/your-username).*
