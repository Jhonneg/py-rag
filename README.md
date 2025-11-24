# Python RAG with LangChain and Pinecone

This project demonstrates a Retrieval-Augmented Generation (RAG) pipeline using Python. It loads documents from various sources, chunks them, and prepares them for vector embedding and storage in a Pinecone vector database.

The project is structured within two main Jupyter notebooks:
-   [main.ipynb](main.ipynb): Handles document loading (PDFs, DOCX, Wikipedia), text chunking, and embedding cost calculation.
-   [pinecone.ipynb](pinecone.ipynb): Manages interaction with the Pinecone vector database.

## Features

-   Load documents from local PDF and DOCX files.
-   Fetch and load data directly from Wikipedia.
-   Split documents into manageable chunks for processing.
-   Calculate the estimated cost of creating embeddings using OpenAI's models.
-   Integrates with Pinecone for vector storage and retrieval.

## Setup

1.  **Clone the repository**
    ```sh
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**
    The necessary packages are installed directly from the notebooks. Run the `pip install` cells in [main.ipynb](main.ipynb) and [pinecone.ipynb](pinecone.ipynb).

4.  **Environment Variables**
    Create a `.env` file in the root of the project and add your API keys. This file is ignored by Git.
    ```
    # .env
    PINECONE_API_KEY="your_pinecone_api_key"
    OPENAI_API_KEY="your_openai_api_key" # Required for embeddings
    ```

5.  **Add Documents**
    Place your PDF or DOCX files inside the `pdfs/` directory.

## Usage

1.  **Process Documents**: Open and run the cells in [main.ipynb](main.ipynb) to load and chunk your documents. You can see the number of chunks created and the estimated embedding cost.

2.  **Manage Vector Database**: Open and run the cells in [pinecone.ipynb](pinecone.ipynb) to set up your Pinecone index and (in a future step) upload the document vectors.

## Demo 

**Question and Answer demo**
<img width="1632" height="403" alt="screenshot-2025-11-24_08-39-35" src="https://github.com/user-attachments/assets/6c97cd02-cedd-4604-ac70-8fae90d66b8b" />
**Chat history demo**
<img width="1829" height="279" alt="screenshot-2025-11-24_08-43-51" src="https://github.com/user-attachments/assets/b0a56913-6b3b-4f4a-829f-417c8eafce6e" />
