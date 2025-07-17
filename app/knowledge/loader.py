import os
from typing import List, Tuple

KNOWLEDGE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'knowledgebase')

CHUNK_SIZE = 500

def load_knowledge_chunks() -> List[Tuple[str, str]]:
    chunks = []
    for fname in os.listdir(KNOWLEDGE_DIR):
        if fname.endswith('.md') or fname.endswith('.txt'):
            with open(os.path.join(KNOWLEDGE_DIR, fname), 'r', encoding='utf-8') as f:
                text = f.read()
                for i in range(0, len(text), CHUNK_SIZE):
                    chunk = text[i:i+CHUNK_SIZE]
                    chunks.append((chunk, fname))
    return chunks 