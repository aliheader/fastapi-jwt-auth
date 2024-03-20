"""Database session handling."""

from sqlalchemy.orm import sessionmaker, Session
from app.db.service.engine import engine


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Get database session.

    Yields:
        (Session): Current SQLAlchemy session.
    """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
