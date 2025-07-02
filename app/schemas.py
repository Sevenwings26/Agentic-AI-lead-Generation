from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SubmitContext(BaseModel):
    full_name: str
    email: str
    # phone_no: Optional[str] = None  
    phone_no: str  # it's important
    intent: str
    property_type: str
    location: str
    budget: float
    additional_notes: Optional[str] = None

    # improve for outbound 
    lead_type: str = "inbound" or "scraped"
    score: Optional[int] = None
    source_url: Optional[str] = None
    # created_at: datetime


# New schema for the API response
class LeadResponse(BaseModel):
    name: str
    message: str
    lead_id: int


