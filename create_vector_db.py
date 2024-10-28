import os
import shutil
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

def create_vector_db(pdf_path, db_directory):
    # Delete existing vector database if it exists
    if os.path.exists(db_directory):
        print(f"The vector database already exists at {db_directory}. Deleting it...")
        shutil.rmtree(db_directory)
        print(f"Deleted the existing vector database at {db_directory}.")

    # Load the PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split the documents into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    # Load the embeddings model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create the vector database without deprecated settings
    vectordb = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory=db_directory,
    )

    print(f"Vector database created at {db_directory}")

# Create vector database for PEI.pdf
create_vector_db("PEI.pdf", "./vector_db_PEI")

# Create vector database for guia.pdf
create_vector_db("guia.pdf", "./vector_db_guia")
