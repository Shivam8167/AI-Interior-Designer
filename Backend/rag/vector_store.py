from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from load_doc import load_documents
import os

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Absolute path to chroma_db
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

print("Chroma DB Path:", CHROMA_PATH)

docs = load_documents()

print("Documents loaded:", len(docs))

db = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory=CHROMA_PATH
)

print("Database count:", db._collection.count())
print("Vector database created successfully!")