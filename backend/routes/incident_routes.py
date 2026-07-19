from fastapi import APIRouter, HTTPException
from models.incident_models import IncidentCreate
from schemas.responses import (
    SuccessResponse,
    ErrorResponse,
)
from services.incident_service import IncidentService
from services.rule_engine import RuleEngine
from services.websocket_manager import manager

router = APIRouter(
    prefix="/incidents",
    tags=["Incident Management"],
)

@router.post(
    "/",
    response_model=SuccessResponse,
)
async def create_new_incident(
    incident: IncidentCreate,
):
    created = IncidentService.create(
        incident
    )
    decision = RuleEngine().evaluate(
        incident=created
    )
    event = {
        "type": "NEW_INCIDENT",
        "payload": {
            "incident": created,
            "decision": decision,
        },
    }
    await manager.broadcast(
        event
    )
    return SuccessResponse(
        success=True,
        message="Incident created successfully.",
        data={
            "incident": created,
            "decision": decision,
        },
    )

@router.get(
    "/",
    response_model=SuccessResponse,
)
def list_incidents():
    return SuccessResponse(
        success=True,
        message="Incident list fetched.",
        data={
            "incidents": IncidentService.get_all()
        },
    )

@router.get(
    "/{incident_id}",
    response_model=SuccessResponse,
    responses={
        404: {
            "model": ErrorResponse
        }
    },
)
def get_incident(
    incident_id: int,
):
    incident = IncidentService.get(
        incident_id
    )
    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found.",
        )
    return SuccessResponse(
        success=True,
        message="Incident fetched.",
        data={
            "incident": incident
        },
    )