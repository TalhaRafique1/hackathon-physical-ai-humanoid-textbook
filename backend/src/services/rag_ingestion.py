import os
from pathlib import Path
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
COLLECTION_NAME = "textbook_rag"
DOCS_PATH = Path("docusaurus/docs")

def get_qdrant_client():
    if QDRANT_API_KEY:
        return QdrantClient(host=QDRANT_HOST, api_key=QDRANT_API_KEY)
    else:
        return QdrantClient(host=QDRANT_HOST)

def process_markdown_file(file_path: Path):
    """Placeholder for processing a single markdown file."""
    content = file_path.read_text(encoding="utf-8")
    # In a real scenario, you'd chunk this content
    # For now, we'll treat the whole file as one chunk
    return {"text": content, "source": str(file_path)}

def generate_embedding(text: str):
    """Placeholder for generating an embedding."""
    # In a real scenario, you'd use an actual embedding model (e.g., from OpenAI, Hugging Face)
    # For now, return a dummy embedding
    return [0.1] * 128  # Example: 128-dimensional embedding

def ingest_documents_to_qdrant():
    client = get_qdrant_client()

    # Create collection if it doesn't exist
    try:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=128, distance=models.Distance.COSINE), # Must match embedding size
        )
        print(f"Collection '{COLLECTION_NAME}' created.")
    except Exception as e:
        print(f"Collection '{COLLECTION_NAME}' already exists or failed to create: {e}")

    points = []
    for md_file in DOCS_PATH.rglob("*.md"):
        if md_file.is_file():
            doc_data = process_markdown_file(md_file)
            embedding = generate_embedding(doc_data["text"])
            
            points.append(
                models.PointStruct(
                    vector=embedding,
                    payload={"text": doc_data["text"], "source": doc_data["source"]}
                )
            )
    
    if points:
        client.upsert(
            collection_name=COLLECTION_NAME,
            wait=True,
            points=points
        )
        print(f"Ingested {len(points)} documents into Qdrant collection '{COLLECTION_NAME}'.")
    else:
        print("No markdown documents found to ingest.")

if __name__ == "__main__":
    ingest_documents_to_qdrant()
