from dotenv import load_dotenv
import os

load_dotenv()

AZURE_AI_ENDPOINT = os.getenv("AZURE_AI_ENDPOINT")
AZURE_AI_API_KEY = os.getenv("AZURE_AI_API_KEY")
AZURE_AI_MODEL = os.getenv("AZURE_AI_MODEL")

if not AZURE_AI_ENDPOINT or not AZURE_AI_API_KEY or not AZURE_AI_MODEL:
    raise ValueError(
        "Missing Azure AI configuration. Check your .env file."
    )
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_STORAGE_CONTAINER_NAME = os.getenv("AZURE_STORAGE_CONTAINER_NAME")    