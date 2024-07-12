import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum

from database import Base

class Sex(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"

class User(Base):
    __tablename__ = 'Users'

    sid = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    dob = Column(DateTime(timezone=True), nullable=False)
    gender = Column(Enum(Sex), nullable=False)
    bio = Column(String, nullable=True)

