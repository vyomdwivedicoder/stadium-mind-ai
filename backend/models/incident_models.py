from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

IncidentType = Literal[
    "crowd_congestion",
    "medical_emergency",
    "security_alert",
    "fire_alert",
    "equipment_failure",
    "navigation_issue"
]

IncidentStatus = Literal[
    "ACTIVE",
    "IN_PROGRESS",
    "RESOLVED"
]

class IncidentCreate(BaseModel):
    type: IncidentType
    location: str = Field(
        min_length=2,
        max_length=100
    )
    severity: int = Field(
        ge=1,
        le=10
    )
    description: str = Field(
        min_length=5,
        max_length=500
    )

class Incident(BaseModel):
    id: int
    type: IncidentType
    location: str
    severity: int
    description: str
    status: IncidentStatus
    created_at: datetime