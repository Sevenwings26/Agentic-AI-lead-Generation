from fastapi import FastAPI, Request, Depends, BackgroundTasks, HTTPException
from fastapi.templating import Jinja2Templates
from schemas import SubmitContext, LeadResponse
from database import engine, get_db
import models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from crud import fetch_leads
import traceback

models.Base.metadata.create_all(bind=engine)

# initialize app 
app = FastAPI()

# CORS headers 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

# load template 
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {'request':request})
    # return "Hello Real Estate..."

"""Inbound leads via forms for visiting users.""" 
@app.post("/submit-lead", response_model=LeadResponse)
async def submit_lead(request: SubmitContext, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    try:
        lead = fetch_leads(db, request.full_name, request.email, request.phone_no, request.intent, request.property_type, request.location, request.budget, request.additional_notes)

        return LeadResponse(
            name=lead.full_name,
            message=f"Lead submitted successfully! Thanks {lead.full_name.split()[0]}",
            lead_id=lead.id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500, 
            detail=f"An unexpected error occurred: {str(e)}"
        )
