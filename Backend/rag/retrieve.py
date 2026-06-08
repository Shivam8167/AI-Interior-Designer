from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Same absolute path as vector_store.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

print("Chroma DB Path:", CHROMA_PATH)

db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)

print("Database count:", db._collection.count())

def get_context(query):
    docs = db.similarity_search(query, k=3)

    print("\nQuery:", query)
    print("Docs found:", len(docs))

    print("\nRetrieved Files:")
    for doc in docs:
        print(doc.metadata.get("source"))

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    return context