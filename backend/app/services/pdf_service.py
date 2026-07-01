from io import BytesIO
from pypdf import PdfReader


class PDFService:
    def extract_text(self, file_data: bytes) -> str:
        pdf = PdfReader(BytesIO(file_data))

        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text


pdf_service = PDFService()