from datetime import timedelta
from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.api.auth.model import Token
from app.api.user.models import UserOut
from app.api.user.service import get_user
from app.core import security
from app.core.config import Settings
from app.db.service.session import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/access-token")


def authenticate(session: Session, username: str, password: str) -> Token:
    user = get_user(session, username)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not security.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    access_token_expires = timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return Token(
        access_token=security.create_access_token(
            user.username, expires_delta=access_token_expires
        )
    )


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserOut:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = security.decode_token(token)
    username: str = payload.get("sub", None)

    if username is None:
        raise credentials_exception

    with SessionLocal() as session:
        user = get_user(session, username)
        session.close()

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    user = UserOut(**user.dict())
    return user
