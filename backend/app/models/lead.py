from sqlalchemy import Column, Integer, String, Date
from app.database.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))
    phone = Column(String(20))
    interest = Column(String(200))
    status = Column(String(20), default="NEW")
    score = Column(Integer, default=0)
    category = Column(String(20), default="COLD")
    notes = Column(String(500), default="")
    follow_up = Column(Date, nullable=True)