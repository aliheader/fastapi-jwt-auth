from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.api.auth import service
from app.api.auth.model import Token
from app.db.service.session import get_db

router = APIRouter()


@router.post("/auth/access-token")
def login_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: Session = Depends(get_db),
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    token = service.authenticate(
        session=session, username=form_data.username, password=form_data.password
    )

    return token
