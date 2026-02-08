from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from app.config import PDF_PATH, VECTOR_DB_PATH, EMBEDDING_MODEL

import os

 

# Check file exists BEFORE loading
if not os.path.exists(PDF_PATH):
    raise FileNotFoundError(f"❌ PDF not found at path: {PDF_PATH}")

print("Loading regulatory PDF...")

loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

print(f"Loaded {len(documents)} pages")

 

print("\n Chunking TEXT into smaller pieces")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,      # Larger chunks = better legal context
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


 
print("\n Loading local embedding model...")
 

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)


 

print("\n Creating FAISS vector database...")

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

vectorstore.save_local(VECTOR_DB_PATH)


print("VECTOR DATABASE CREATED!")

 
