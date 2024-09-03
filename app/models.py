from .database import Base
from sqlalchemy import ForeignKey, Integer, String, Boolean, Column, TIMESTAMP
from datetime import datetime


class Posts(Base): 
    __tablename__ = "Posts"
    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    added_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=(('now()')))

    owner_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)

class Users(Base): 
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String, nullable=True)
    email  = Column(String, nullable=True)
    password = Column(String, nullable=False)
    joined_date = Column(TIMESTAMP(timezone=True), nullable=False, server_default=(('now()')))
