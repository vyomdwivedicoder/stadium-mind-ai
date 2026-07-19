from typing import Literal, Any
from pydantic import BaseModel

RiskLevel = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]

class AIAnalysis(BaseModel):
    summary: str
    risk_level: RiskLevel | str
    recommended_action: str
    predicted_outcome: str

class AIResponse(BaseModel):
    success: bool
    analysis: AIAnalysis

class AIRequest(BaseModel):
    incident: dict[str, Any]