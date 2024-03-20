from sqlalchemy import Boolean, Column, Integer, String
from app.db.models.base import TableBase


class User(TableBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
