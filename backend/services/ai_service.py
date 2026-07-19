import json
from typing import Any
from groq import Groq
from config import settings
from utils.logger import logger

class AIService:
    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )
        self.model = settings.GROQ_MODEL

    def build_prompt(
        self,
        incident: dict[str, Any]
    ) -> str:
        return f"""
You are StadiumMind AI.
You are the AI Command Center responsible for managing incidents
inside a FIFA World Cup stadium.
Your task is to analyze the incident and provide operational advice.
Incident
Type:
{incident["type"]}
Location:
{incident["location"]}
Severity:
{incident["severity"]}/10
Description:
{incident["description"]}
Return ONLY valid JSON.
Use this exact format.
{{
    "summary":"",
    "risk_level":"",
    "recommended_action":"",
    "predicted_outcome":""
}}
Do not include markdown.
Do not explain anything.
Only output JSON.
"""

    def analyze(
        self,
        incident: dict[str, Any]
    ) -> dict:
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                temperature=0.2,
                response_format={
                    "type": "json_object"
                },
                messages=[
                    {
                        "role": "system",
                        "content":
                            "You are an expert Stadium Operations AI."
                    },
                    {
                        "role": "user",
                        "content":
                            self.build_prompt(
                                incident
                            )
                    }
                ]
            )
            message = (
                completion
                .choices[0]
                .message
                .content
            )
            if message is None:
                raise RuntimeError(
                    "Empty AI response."
                )
            analysis = json.loads(
                message
            )
            logger.info(
                "AI analysis completed."
            )
            return analysis
        except Exception as e:
            logger.exception(e)
            return {
                "summary":
                    "AI analysis unavailable.",
                "risk_level":
                    "UNKNOWN",
                "recommended_action":
                    "Escalate to human operators.",
                "predicted_outcome":
                    "Unknown"
            }

ai_service = AIService()