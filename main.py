from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from app.controllers.upload import router as upload_router
from app.core.middleware import handle_exceptions

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=handle_exceptions)
app.include_router(upload_router, prefix="/upload")
