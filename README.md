# RAG with Python, LangChain, and Vector Databases

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using Python, LangChain, and OpenAI. It can load PDF documents, create vector embeddings, and store them in a vector database like ChromaDB or Pinecone for efficient retrieval and question-answering. The project includes Jupyter notebooks for development and a Streamlit application for an interactive user interface.

## Features

-   **Document Loading**: Load and process text from local PDF files.
-   **Text Chunking**: Split documents into smaller, manageable chunks suitable for embedding.
-   **Vector Embeddings**: Generate vector embeddings using OpenAI's models.
-   **Vector Storage**:
    -   [ChromaDB](https://www.trychroma.com/) for local, persistent vector storage.
    -   [Pinecone](https://www.pinecone.io/) for a cloud-based, scalable vector database.
-   **Conversational Interface**: Ask questions about the loaded documents through a Streamlit web app.
-   **Cost Estimation**: Provides an estimated cost for generating embeddings before processing.

## Project Structure

```
.
├── .env                  # Environment variables (API keys)
├── main.ipynb            # Jupyter notebook for ChromaDB workflow
├── pinecone.ipynb        # Jupyter notebook for Pinecone management
├── streamlit_app.py      # The Streamlit web application
├── requirements.txt      # Python dependencies
├── pdfs/                 # Directory for your PDF documents
└── chroma_db/            # Local storage for ChromaDB
```

## Setup

Follow these steps to set up and run the project locally.

1.  **Clone the Repository**
    ```sh
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    Install the required packages from the `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```

4.  **Environment Variables**
    Create a `.env` file in the root directory and add your API keys. This file is ignored by Git.
    ```
    # .env
    OPENAI_API_KEY="your_openai_api_key"
    PINECONE_API_KEY="your_pinecone_api_key"
    ```

5.  **Add Documents**
    Place the PDF files you want to process inside the `pdfs/` directory.

## Usage

You can interact with this project using the Jupyter notebooks or the Streamlit web application.

### 1. Jupyter Notebooks

-   **[main.ipynb](main.ipynb)**: Use this notebook to step through the process of loading documents, chunking them, and storing the embeddings in a local ChromaDB instance.
-   **[pinecone.ipynb](pinecone.ipynb)**: This notebook demonstrates how to create, manage, and query a Pinecone index for your vector embeddings.

### 2. Streamlit Application

For an interactive experience, run the Streamlit app. This allows you to upload a document and ask questions about its content.

1.  Launch the application from your terminal:
    ```sh
    streamlit run streamlit_app.py
    ```
2.  Open your web browser to the local URL provided by Streamlit.
3.  Upload a PDF document and start asking questions.
