from fastapi import FastAPI
from .api import rag

app = FastAPI()

app.include_router(rag.router)

@app.get("/")
async def root():
    return {"message": "Physical AI & Humanoid Robotics Textbook Backend"}
