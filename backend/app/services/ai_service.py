from email import contentmanager
from openai import OpenAI
from app.core.config import (
    AZURE_AI_ENDPOINT,
    AZURE_AI_API_KEY,
    AZURE_AI_MODEL,
)
import json


class AIService:
    def __init__(self):
        self.client = OpenAI(
            base_url=AZURE_AI_ENDPOINT,
            api_key=AZURE_AI_API_KEY,
        )

    def chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=AZURE_AI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are TalentOS, an AI hiring assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
        )

        return response.choices[0].message.content

    def parse_resume(self, resume_text: str) -> str:
        response = self.client.chat.completions.create(
            model=AZURE_AI_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        """
You are an expert AI recruitment assistant.

Extract the following information from the resume.

Return ONLY valid JSON.

{
    "name": "",
    "email": "",
    "phone": "",
    "education": [],
    "experience": [],
    "skills": [],
    "summary": ""
}

Do not include explanations.
Do not use markdown.
Do not wrap the JSON in ``` blocks.
"""
                    ),
                },
                {
                    "role": "user",
                    "content": resume_text,
                },
            ],
            temperature=0,
        )
        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {
                "error": "Model did not return valid JSON.",
                "raw_response": content
    }

        
    

     
     


    

ai_service = AIService()