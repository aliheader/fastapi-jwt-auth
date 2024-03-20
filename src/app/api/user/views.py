from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.auth.service import get_current_user
from app.api.user import service
from app.api.user.models import User, UserCreate, UserOut
from app.db.service.session import get_db

router = APIRouter()


@router.post("/users/", response_model=User, status_code=201)
def create_user(
    user_data: UserCreate,
    session: Session = Depends(get_db),
):
    db_user = service.create_user(session, user_data)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User does not found")

    user = UserOut(**db_user.model_dump())

    return user


@router.get("/users/", response_model=UserOut)
def read_user(
    current_user: Annotated[User, Depends(get_current_user)],
):

    return current_user
