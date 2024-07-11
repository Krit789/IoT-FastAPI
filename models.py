import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum
# from sqlalchemy.orm import relationship

from database import Base

class Sex(enum.Enum):
    male = "MALE"
    female = "FEMALE"
    other = "OTHER"

class User(Base):
    __tablename__ = 'Users'

    sid = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(DateTime(timezone=True))
    sex = Column(Enum(Sex))
    bio = Column(String)

