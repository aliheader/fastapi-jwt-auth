from sqlalchemy.orm import Session
from app.api.user import models
from app.core.security import get_hashed_password
from app.db.models.user import User


def get_user(session: Session, username: str) -> User:
    db_user = session.query(User).filter(User.username == username).first()

    return db_user


def create_user(session: Session, user: models.UserCreate):
    db_user_data = user.model_dump()

    db_user_data["is_active"] = True
    db_user_data["hashed_password"] = get_hashed_password(db_user_data["password"])
    del db_user_data["password"]
    del db_user_data["confirm_password"]

    db_user = User(**db_user_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    user = models.User(**db_user.dict())

    return user
