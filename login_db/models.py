
import uuid
from datetime import datetime

from login_db.enums import TokenStatus, TokenType, UserStatus
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base

# Define the base model
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True,  unique=True, nullable=False, default=lambda: uuid.uuid4().hex)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    status = Column(Enum(UserStatus), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    # TODO: add the following columns
    #last_login = Column(DateTime, nullable=True, default=None)
    #last_password_change = Column(DateTime, nullable=True, default=None)
    #last_username_change = Column(DateTime, nullable=True, default=None)

class Token(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    token = Column(String, unique=True, nullable=False)
    type = Column(Enum(TokenType), nullable=False)
    expiration_time = Column(DateTime, nullable=False)
    status = Column(Enum(TokenStatus), nullable=False)
    # TODO: add the following columns
    #created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    #updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    #last_used_at = Column(DateTime, nullable=True, default=None)
