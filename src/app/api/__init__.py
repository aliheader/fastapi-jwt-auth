from fastapi import APIRouter
from app.api.auth.views import router as auth_router
from app.api.user.views import router as user_router

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(auth_router)
