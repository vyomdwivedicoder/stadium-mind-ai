from typing import Any
from pydantic import BaseModel

class SuccessResponse(
    BaseModel,
):
    success: bool = True
    message: str
    data: Any

class ErrorResponse(
    BaseModel,
):
    success: bool = False
    message: str