import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from qdrant_client import QdrantClient, models
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
COLLECTION_NAME = "textbook_rag"

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    user_id: Optional[str] = None

class QueryResponse(BaseModel):
    response: str
    sources: List[str]

def get_qdrant_client():
    if QDRANT_API_KEY:
        return QdrantClient(host=QDRANT_HOST, api_key=QDRANT_API_KEY)
    else:
        return QdrantClient(host=QDRANT_HOST)

def generate_embedding(text: str):
    """Placeholder for generating an embedding for a query."""
    # In a real scenario, this would use the same model as ingestion
    return [0.1] * 128  # Example: 128-dimensional embedding

@router.post("/query", response_model=QueryResponse)
async def query_rag_chatbot(request: QueryRequest):
    if not request.query:
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    client = get_qdrant_client()
    query_embedding = generate_embedding(request.query)

    try:
        search_result = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=3  # Get top 3 relevant documents
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Qdrant search failed: {e}")

    # Placeholder for generating a response based on search results
    if search_result:
        sources = [point.payload.get("source", "unknown") for point in search_result]
        context = " ".join([point.payload.get("text", "") for point in search_result])
        
        # In a real scenario, you'd feed 'request.query' and 'context' to an LLM
        # to generate a more sophisticated response.
        response_text = f"This is a placeholder response for your query: '{request.query}'. Relevant content found from sources: {', '.join(sources)}."
    else:
        response_text = "No relevant information found in the textbook."
        sources = []

    return QueryResponse(response=response_text, sources=sources)

