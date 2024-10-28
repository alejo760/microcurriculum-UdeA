# create_vector_db.py

import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def create_vector_db(pdf_path, db_directory):
    # Verificar si la base de datos ya existe
    if os.path.exists(db_directory):
        print(f"La base de datos vectorial ya existe en {db_directory}")
        return

    # Cargar el PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Dividir el documento en trozos manejables
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    # Cargar el modelo de embeddings
    embeddings = HuggingFaceEmbeddings()

    # Crear la base de datos vectorial
    vectordb = Chroma.from_documents(docs, embeddings, persist_directory=db_directory)

    # Guardar la base de datos vectorial
    vectordb.persist()
    print(f"Base de datos vectorial creada en {db_directory}")

# Crear base de datos para PEI.pdf
create_vector_db("PEI.pdf", "./vector_db_PEI")

# Crear base de datos para guia.pdf
create_vector_db("guia.pdf", "./vector_db_guia")
