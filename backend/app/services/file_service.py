# pyrefly: ignore [missing-import]
from fastapi import UploadFile,File

class FileService:
    def __init__(self):
        pass
    def upload_file(self,file:UploadFile=File(...)):
        return{
            "filename":file.filename,
            "content_type":file.content_type,
            "file_size":file.size,
            "message":"File uploaded successfully"
            
        }
