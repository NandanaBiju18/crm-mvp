from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.models.lead import Lead

router = APIRouter()

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):

    leads = db.query(Lead).all()

    total = len(leads)

    hot = len([l for l in leads if l.category == "HOT"])

    warm = len([l for l in leads if l.category == "WARM"])

    cold = len([l for l in leads if l.category == "COLD"])

    qualified = len(
        [l for l in leads if l.status == "QUALIFIED"]
    )

    contacted = len(
        [l for l in leads if l.status == "CONTACTED"]
    )

    return {
        "total": total,
        "hot": hot,
        "warm": warm,
        "cold": cold,
        "qualified": qualified,
        "contacted": contacted,
    }