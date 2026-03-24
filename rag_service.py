from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = "data/company_docs.txt"

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_documents():

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return f.read()


def split_documents():

    text = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    return chunks


def build_vector_store():

    chunks = split_documents()

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings))

    return index, chunks


index, chunks = build_vector_store()


def retrieve_context(query):

    query_vector = model.encode([query])

    distances, indices = index.search(query_vector, k=2)

    results = []

    for i in indices[0]:
        results.append(chunks[i])

    return "\n".join(results)