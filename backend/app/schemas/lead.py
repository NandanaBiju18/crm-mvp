from pydantic import BaseModel
from datetime import date

class LeadCreate(BaseModel):
    name: str
    phone: str
    interest: str
    notes: str = ""
    follow_up: date | None = None

class LeadResponse(BaseModel):
    id: int
    name: str
    phone: str
    interest: str
    status: str
    notes: str | None = ""
    follow_up: date | None = None

    class Config:
        from_attributes = True