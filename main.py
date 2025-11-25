import os
from click import prompt
from pinecone import Pinecone
from pinecone import ServerlessSpec
import streamlit as st
from dotenv import load_dotenv, find_dotenv

pc = Pinecone()


def load_document(file):
    name, extension = os.path.splitext(file)

    if extension == ".pdf":
        from langchain_classic.document_loaders import PyPDFLoader

        print(f"Loading {file}")
        loader = PyPDFLoader(file)
    elif extension == ".docx":
        from langchain_classic.document_loaders import Docx2txtLoader

        loader = Docx2txtLoader(file)
    else:
        print("Document format is not supported")
        return None

    data = loader.load()
    return data


def chunk_data(data, chunk_size=256):
    from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=0
    )
    chunks = text_splitter.split_documents(data)
    return chunks


def print_embedding_cost(texts):
    import tiktoken

    enc = tiktoken.encoding_for_model("text-embedding-ada-002")
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    print(f"Total Tokens: {total_tokens}")
    print(f"Embedding Cost in USD: {total_tokens / 1000 * 0.00002:.6f}")


def insert_or_fetch_embeddings(index_name, chunks):
    import pinecone

    # from langchain_community.vectorstores import Pinecone
    from langchain_pinecone.vectorstores import Pinecone
    from langchain_openai import OpenAIEmbeddings
    from pinecone import ServerlessSpec

    pc = pinecone.Pinecone()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1536)

    if index_name in pc.list_indexes().names():
        print(f"Index {index_name} already exists. Loading embeddings...", end="")
        vector_store = Pinecone.from_existing_index(index_name, embeddings)
        print("Ok")
    else:
        print(f"Creating index {index_name} and embeddings...", end="")
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
        vector_store = Pinecone.from_documents(
            chunks, embeddings, index_name=index_name
        )
        print("Ok")
        return vector_store

data = load_document("pdfs/guia_lgpd.pdf")
# print(data[1].page_content)

print(f"You have {len(data)} pages in your data")

chunks = chunk_data(data)
print(len(chunks))
print(chunks[10].page_content)
print_embedding_cost(chunks)
index_name = "askadocument"
vector_store = insert_or_fetch_embeddings(index_name, chunks)