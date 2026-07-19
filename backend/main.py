from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings

from routes.incident_routes import router as incident_router
from routes.ai_routes import router as ai_router
from routes.websocket_routes import router as websocket_router
from middleware.request_logger import (
    RequestLoggerMiddleware
)
from exceptions import (
    register_exception_handlers
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("StadiumMind AI Started")
    yield
    print("StadiumMind AI Stopped")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(
    incident_router,
    prefix="/incidents",
    tags=["Incident Management"]
)


app.include_router(
    ai_router,
    prefix="/ai",
    tags=["AI Command Center"]
)


app.include_router(
    websocket_router,
    tags=["Realtime"]
)

app.add_middleware(
    RequestLoggerMiddleware
)

register_exception_handlers(app)

@app.get("/")
async def home():
    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running"
    }