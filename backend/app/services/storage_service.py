from azure.storage.blob import BlobServiceClient
from app.core.config import (
    AZURE_STORAGE_CONNECTION_STRING,
    AZURE_STORAGE_CONTAINER_NAME,
)
from uuid import uuid4


class StorageService:
    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(
            AZURE_STORAGE_CONNECTION_STRING
        )
        self.container_client = self.blob_service_client.get_container_client(
            AZURE_STORAGE_CONTAINER_NAME
        )


    def upload_resume(self, file_name: str, file_data: bytes) -> str:
        blob_name = f"{uuid4()}_{file_name}"

        blob_client = self.container_client.get_blob_client(blob_name)

        blob_client.upload_blob(file_data, overwrite=True)

        return blob_name        
