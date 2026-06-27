# AI Sales CRM (Level 1 MVP)

An AI-powered Customer Relationship Management (CRM) system that helps educational institutes and sales teams manage leads, prioritize prospects using AI, and generate personalized follow-up messages.

## Features

* 📋 Lead Management (Create, Read, Update, Delete)
* 🤖 AI Lead Scoring
* ✉️ AI Follow-up Message Generation
* 📝 Notes & Follow-up Tracking
* 📊 Dashboard with Lead Statistics
* 🔍 Search and Filter Leads
* 🗄️ MySQL Database Integration
* ⚡ FastAPI Backend
* ⚛️ React Frontend

## Tech Stack

### Frontend

* React
* Axios
* CSS

### Backend

* FastAPI
* SQLAlchemy
* Groq API
* MySQL

### Database

* MySQL

## Project Structure

```
sales-ai-mvp/
│
├── frontend/
│
├── backend/
│   ├── app/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── services/
│   ├── main.py
│   └── requirements.txt
│
└── README.md
```

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd sales-ai-mvp
```

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## AI Features

* AI Lead Scoring based on customer information
* AI-generated personalized follow-up messages
* Automated lead prioritization

## Future Roadmap

### ✅ Level 1 (Completed)

* CRM
* Dashboard
* AI Lead Scoring
* AI Follow-up Generator
* Notes & Follow-up

### 🚀 Level 2 (Planned)

* AI Voice Calling
* Conversation Transcripts
* AI Conversation Analysis
* Customer Report Generation
* WhatsApp Automation



✅ Level 1 MVP

Customer
    ↓
Add Lead
    ↓
MySQL
    ↓
React CRM
    ↓
Lead Dashboard
    ↓
AI Lead Scoring
    ↓
AI Follow-up Message
    ↓
Notes & Follow-ups
    ↓
Analytics Dashboard

