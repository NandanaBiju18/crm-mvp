from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes.leads import router as leads_router
from fastapi.middleware.cors import CORSMiddleware
from app.routes.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads_router)
app.include_router(dashboard_router)
@app.get("/")
def home():
    return {"message": "Sales AI Running"}