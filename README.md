Training Institute CRM MVP.

Stage 1 — Project Setup ✅
Backend Setup
Created FastAPI project
Installed:
FastAPI
Uvicorn
SQLAlchemy
PyMySQL
Connected FastAPI to MySQL
Database Setup

Created database:

CREATE DATABASE sales_ai;
Project Structure
backend/
│
├── app/
│   ├── main.py
│   ├── database/
│   │   ├── database.py
│   │   └── deps.py
│   ├── models/
│   │   └── lead.py
│   ├── routes/
│   │   └── leads.py
│   └── schemas/
│       └── lead.py
Result
✅ FastAPI running
✅ MySQL connected
✅ Swagger Docs working


Stage 2 — Lead CRM ✅
Lead Model

Created Lead table:

Lead
├── id
├── name
├── phone
├── interest
└── status
APIs
Create Lead
POST /leads

Example:

{
  "name": "Rahul",
  "phone": "9876543210",
  "interest": "Data Science"
}
Get All Leads
GET /leads

Returns:

[
  {
    "id": 1,
    "name": "Rahul",
    "phone": "9876543210",
    "interest": "Data Science",
    "status": "NEW"
  }
]
Frontend

Created React + Vite app.

Features:

Name
Phone
Interest
Add Lead
Result
✅ Add Lead
✅ View Leads
✅ FastAPI ↔ React Connected


Stage 3 — Lead Management ✅
Update Lead Status

API:

PUT /leads/{id}

Example:

PUT /leads/1?status=QUALIFIED

Status options:

NEW
CONTACTED
QUALIFIED
INTERESTED
CLOSED
LOST
Delete Lead

API:

DELETE /leads/{id}

Example:

DELETE /leads/1
Search Lead

API:

GET /search?keyword=rah

Searches by lead name.

Frontend Additions

Added:

Search Lead
Status Dropdown
Delete Button

Table:

ID | Name | Phone | Interest | Status | Actions
Result
✅ Add Lead
✅ View Leads
✅ Search Lead
✅ Update Status
✅ Delete Lead
Current MVP Status
Stage 1 ✅ Project Setup
Stage 2 ✅ Lead CRM
Stage 3 ✅ Lead Management

Stage 4 ⏸ AI Lead Scoring
Stage 5 ⏳ Follow-up Management
Stage 6 ⏳ Dashboard Analytics
Stage 7 ⏳ Calling Integration
Stage 8 ⏳ AI Summaries
Stage 9 ⏳ WhatsApp Automation
Stage 10 ⏳ AI Voice Agent
