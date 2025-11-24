import os
from click import prompt
import streamlit as st
import google.generativeai as genai

from dotenv import load_dotenv, find_dotenv

def load_document(file):
    import os

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