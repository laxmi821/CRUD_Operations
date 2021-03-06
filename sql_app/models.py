
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    address = Column(String(100), nullable=False)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(String(100), nullable=False, index=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    owner = relationship("User", back_populates="items")
