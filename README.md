# RAG with Python, LangChain, and Vector Databases

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using Python and LangChain. It loads documents from various sources, splits them into manageable chunks, creates vector embeddings, and stores them in a vector database like Pinecone or ChromaDB for efficient retrieval.

The project is structured into two main Jupyter notebooks:

-   [main.ipynb](main.ipynb): Handles document loading (PDFs, DOCX, Wikipedia), text chunking, embedding cost calculation, and interaction with a ChromaDB vector store.
-   [pinecone.ipynb](pinecone.ipynb): Manages all interactions with the Pinecone vector database, including index creation, upserting vectors, querying, and deleting.

## Features

-   **Document Loading**: Load documents from local PDF files.
-   **Text Chunking**: Split documents into smaller chunks suitable for embedding.
-   **Vector Embeddings**: Create vector representations of text chunks using OpenAI's models.
-   **Cost Estimation**: Calculate the estimated cost for generating embeddings.
-   **Vector Storage**: Integrate with both [ChromaDB](https://www.trychroma.com/) and [Pinecone](https://www.pinecone.io/) for vector storage and retrieval.

## Setup

1.  **Clone the Repository**
    ```sh
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and Activate a Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    Install the required packages by running the `pip install` cells within the [main.ipynb](main.ipynb) and [pinecone.ipynb](pinecone.ipynb) notebooks, or install them from the `requirements.txt` file:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Environment Variables**
    Create a `.env` file in the project root and add your API keys. This file is included in `.gitignore` and will not be committed.
    ```
    # .env
    PINECONE_API_KEY="your_pinecone_api_key"
    OPENAI_API_KEY="your_openai_api_key"
    ```

5.  **Add Documents**
    Place your PDF files inside the `pdfs/` directory.

## Usage

1.  **Process Documents and Use ChromaDB**:
    Open and run the cells in [main.ipynb](main.ipynb) to load documents, split them into chunks, and store the embeddings in a local ChromaDB database.

2.  **Manage Vector Database**: Open and run the cells in [pinecone.ipynb](pinecone.ipynb) to set up your Pinecone index and (in a future step) upload the document vectors.

## Demo 

<div align=center>

**Question and Answer demo**

<img width="1632" height="403" alt="screenshot-2025-11-24_08-39-35" src="https://github.com/user-attachments/assets/6c97cd02-cedd-4604-ac70-8fae90d66b8b" />

**Answering document specific questions**

<img width="1254" height="558" alt="image" src="https://github.com/user-attachments/assets/24e88bd7-3cf4-4b37-b872-ad525c57d0a9" />

**Chat history demo**

<img width="1829" height="279" alt="screenshot-2025-11-24_08-43-51" src="https://github.com/user-attachments/assets/b0a56913-6b3b-4f4a-829f-417c8eafce6e" />

</div>

