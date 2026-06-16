from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import Query
from app.models.lead import Lead
from app.database.deps import get_db
from app.schemas.lead import LeadCreate

router = APIRouter()
@router.post("/leads")
def create_lead(
    data: LeadCreate,
    db: Session = Depends(get_db)
):
    lead = Lead(
        name=data.name,
        phone=data.phone,
        interest=data.interest
    )

    db.add(lead)
    db.commit()
    db.refresh(lead)

    return lead
@router.get("/leads")
def get_leads(
    db: Session = Depends(get_db)
):
    return db.query(Lead).all()

@router.put("/leads/{lead_id}")
def update_status(
    lead_id: int,
    status: str,
    db: Session = Depends(get_db)
):
    lead = db.query(Lead).filter(
        Lead.id == lead_id
    ).first()

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    lead.status = status

    db.commit()
    db.refresh(lead)

    return lead

@router.delete("/leads/{lead_id}")
def delete_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):
    lead = db.query(Lead).filter(
        Lead.id == lead_id
    ).first()

    if not lead:
        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    db.delete(lead)
    db.commit()

    return {"message": "Lead deleted"}

@router.get("/search")
def search_leads(
    keyword: str,
    db: Session = Depends(get_db)
):
    return db.query(Lead).filter(
        Lead.name.contains(keyword)
    ).all()