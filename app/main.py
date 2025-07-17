from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.knowledge.loader import load_knowledge_chunks
from app.knowledge.embedder import get_embedding
from app.knowledge.vector_store import InMemoryVectorStore
from app.chatbot.rag_chain import RAGChain

app = FastAPI()

vector_store = InMemoryVectorStore()
rag_chain = None

class ChatRequest(BaseModel):
    question: str

@app.on_event("startup")
def startup_event():
    global rag_chain
    chunks = load_knowledge_chunks()
    for chunk, fname in chunks:
        emb = get_embedding(chunk)
        vector_store.add(emb, chunk, fname)
    rag_chain = RAGChain(vector_store)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat")
def chat(req: ChatRequest):
    if not rag_chain:
        raise HTTPException(status_code=503, detail="RAGChain not initialized.")
    answer = rag_chain.answer(req.question)
    return {"answer": answer} 