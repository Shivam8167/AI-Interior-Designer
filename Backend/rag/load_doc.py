from langchain_community.document_loaders import TextLoader
import os

def load_documents():
    docs = []

    current_dir = os.path.dirname(__file__)

    kb_path = os.path.abspath(
        os.path.join(current_dir, "..", "knowledge_base")
    )

    print("Loading from:", kb_path)

    for file in os.listdir(kb_path):
        if file.endswith(".txt"):
            loader = TextLoader(
                os.path.join(kb_path, file),
                encoding="utf-8"
            )

            docs.extend(loader.load())

    return docs

documents = load_documents()

print(f"Loaded {len(documents)} documents")