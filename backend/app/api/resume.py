from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.storage_service import StorageService
from app.services.pdf_service import pdf_service
from app.services.ai_service import ai_service

router = APIRouter(prefix="/resume", tags=["Resume"])

storage_service = StorageService()


@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_data = await file.read()

    # Extract text from the PDF
    resume_text = pdf_service.extract_text(file_data)

    # Upload original PDF to Azure Blob Storage
    blob_name = storage_service.upload_resume(
        file.filename,
        file_data
    )

    # Ask Phi to analyze the resume
    candidate_info = ai_service.parse_resume(resume_text)

    return {
        "message": "Resume uploaded and analyzed successfully.",
        "blob_name": blob_name,
        "candidate": candidate_info
    }