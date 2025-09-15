from sqlalchemy import column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"
    
    
    id = column(Integer, primary_key=True, index=True)
    username = column(String, unique=True, index=True)
    email = column(String, unique=True, index=True)
    hashed_password = column(String)
    
    