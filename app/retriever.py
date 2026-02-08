from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import VECTOR_DB_PATH, EMBEDDING_MODEL

import os


def get_retriever():

    if not os.path.exists(VECTOR_DB_PATH):
        raise FileNotFoundError(
            "Vector DB not found. Run ingest.py first."
        )

    print("Loading vector database")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    db = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Number of chunks retrieved per query
    retriever = db.as_retriever(
        search_kwargs={"k": 2}
    )

    return retriever
