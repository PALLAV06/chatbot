from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    AZURE_OPENAI_API_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_DEPLOYMENT: str
    AZURE_SEARCH_API_KEY: str
    AZURE_SEARCH_ENDPOINT: str
    AZURE_SEARCH_INDEX: str
    CONFLUENCE_BASE_URL: str
    CONFLUENCE_API_TOKEN: str
    CONFLUENCE_USERNAME: str

    class Config:
        env_file = ".env"

settings = Settings() 