from pydantic import BaseModel

class LeadCreate(BaseModel):
    name: str
    phone: str
    interest: str

class LeadResponse(BaseModel):
    id: int
    name: str
    phone: str
    interest: str
    status: str

    class Config:
        from_attributes = True