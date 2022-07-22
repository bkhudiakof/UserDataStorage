from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from ..db_setup import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)
    register_date = Column(DateTime, default=datetime.utcnow, nullable=False)
