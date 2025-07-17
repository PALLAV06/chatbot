from app.knowledge.embedder import get_embedding
from app.knowledge.vector_store import InMemoryVectorStore
from app.config import settings
import openai

class RAGChain:
    def __init__(self, vector_store: InMemoryVectorStore):
        self.vector_store = vector_store
        self.llm_deployment = settings.AZURE_OPENAI_DEPLOYMENT

    def answer(self, question: str) -> str:
        # Embed the question
        q_emb = get_embedding(question)
        # Retrieve top 3 relevant chunks
        top_chunks = self.vector_store.search(q_emb, top_k=3)
        context = "\n".join([chunk for chunk, _, _ in top_chunks])
        prompt = f"You are a helpful assistant. Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:"
        response = openai.ChatCompletion.create(
            engine=self.llm_deployment,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=256,
            temperature=0.2
        )
        return response['choices'][0]['message']['content'].strip() 