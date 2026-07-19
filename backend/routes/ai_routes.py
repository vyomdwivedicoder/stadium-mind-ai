from fastapi import APIRouter
from models.ai_models import AIRequest
from schemas.responses import SuccessResponse
from services.ai_service import ai_service

router = APIRouter(
    prefix="/ai",
    tags=["AI Command Center"],
)

@router.post(
    "/analyze",
    response_model=SuccessResponse,
)
def analyze(request: AIRequest):

    result = ai_service.analyze(
        request.incident
    )
    return SuccessResponse(
        success=True,
        message="AI analysis completed.",
        data=result,
    )