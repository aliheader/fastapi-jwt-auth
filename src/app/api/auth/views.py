from datetime import timedelta
from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.auth.model import Token
from app.api.auth import service
from app.api.user.models import UserOut
from app.db.service.session import get_db
from app.core import security


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


# @router.post("/auth/test-token", response_model=UserOut)
# def test_token(current_user: CurrentUser) -> Any:
#     """
#     Test access token
#     """
#     return current_user
