import openai
from app.config import settings

openai.api_key = settings.AZURE_OPENAI_API_KEY
openai.api_base = settings.AZURE_OPENAI_ENDPOINT
openai.api_type = "azure"
openai.api_version = "2023-05-15"

EMBEDDING_DEPLOYMENT = settings.AZURE_OPENAI_DEPLOYMENT


def get_embedding(text: str) -> list:
    response = openai.Embedding.create(
        input=text,
        engine=EMBEDDING_DEPLOYMENT
    )
    return response['data'][0]['embedding'] 