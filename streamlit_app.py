import os
import shutil
from langchain_openai import ChatOpenAI
from pinecone import Pinecone, ServerlessSpec
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import tempfile
from langchain_classic.chains.conversational_retrieval.base import (
    ConversationalRetrievalChain,
)
from langchain_classic.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from langchain_classic.chains.conversational_retrieval.base import (
    ConversationalRetrievalChain,
)
from langchain_classic.memory import ConversationBufferMemory


load_dotenv(find_dotenv(), override=True)

pc = Pinecone()


# -----------------Util functions-----------------
# Doc loading
@st.cache_data
def load_document(file):
    extension = Path(file).suffix
    if extension == ".pdf":
        from langchain_community.document_loaders import PyPDFLoader

        st.write(f"Loading {file}")
        loader = PyPDFLoader(file)
    elif extension == ".docx":
        from langchain_classic.document_loaders import Docx2txtLoader

        st.write(f"Loading {file}")
        loader = Docx2txtLoader(file)
    else:
        st.write("Document format is not supported")
        return None
    data = loader.load_and_split()
    return data


# Chunking
def chunk_data(data, chunk_size=256):
    from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=0
    )
    chunks = text_splitter.split_documents(data)
    return chunks


# Embedding cost


def print_embedding_cost(texts):
    import tiktoken

    enc = tiktoken.encoding_for_model("text-embedding-ada-002")
    total_tokens = sum([len(enc.encode(page.page_content)) for page in texts])
    print(f"Total Tokens: {total_tokens}")
    print(f"Embedding Cost in USD: {total_tokens / 1000 * 0.00002:.6f}")
    return total_tokens


# Create or load vector db


def insert_or_fetch_embeddings(index_name, chunks):
    import pinecone

    # from langchain_community.vectorstores import Pinecone
    from langchain_pinecone.vectorstores import Pinecone
    from langchain_openai import OpenAIEmbeddings

    pc = pinecone.Pinecone()
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1536)

    if index_name in pc.list_indexes().names():
        print(f"Index {index_name} already exists. Loading embeddings...", end="")
        vector_store = Pinecone.from_existing_index(index_name, embeddings)
        print("Ok")
        return vector_store
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


# Create CRC
def chat_with_history(vector_store):
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

    llm = ChatOpenAI(model="gpt-5", temperature=0)
    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwards={"k": 5}
    )
    # prompt = ChatPromptTemplate.from_messages(
    #     [
    #         MessagesPlaceholder(variable_name="chat_history"),
    #         ("user", "{input}"),
    #         (
    #             "user",
    #             "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation",
    #         ),
    #     ]
    # )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    crc = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=retriever, memory=memory, chain_type="stuff", verbose=True
    )
    return crc


# -------- Streamlit ---------

working_dir = os.getcwd()

st.subheader("Document RAG Demo")

file = st.file_uploader("Upload PDF or DOCX ", type=["pdf", "docx"])

if file is not None:
    temp_file = "./temp.pdf"
    file_path = f"{working_dir}/{file.name}"
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
        shutil.copyfileobj(file, tmpfile)
        file_path = tmpfile.name

    data = load_document(file_path)
    st.write(f"Your file has {len(data)} pages")
    chunks = chunk_data(data)
    embed_cost = print_embedding_cost(chunks)
    st.write(f"This document will cost {embed_cost / 1000 * 0.00002:.6f}USD to embed")
    index_name = "askadocument"
    vector_store = insert_or_fetch_embeddings(index_name, chunks)

    question = st.chat_input("Ask the document anything")
    if question:
        with st.spinner("Loading"):
            if "history" not in st.session_state:
                st.session_state.history = ""
            crc = chat_with_history(vector_store)
            answer = crc.invoke(
                {"chat_history": st.session_state.history, "question": question}
            )
            value = f"Q: {question} \n\n A: {answer['answer']}"
            st.session_state.history = (
                f"{value} \n\n {'-' * 100} \n\n {st.session_state.history}"
            )
            h = st.session_state.history
            st.text_area("Response: ", value=answer["answer"])
            st.divider()
            st.text_area(label="Chat history", value=h, height=400, key="history")
