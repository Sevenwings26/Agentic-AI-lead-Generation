from pydantic import BaseModel
from typing import Optional

class SubmitContext(BaseModel):
    full_name: str
    email: str
    phone_no: Optional[str] = None
    intent: str
    property_type: str
    location: str
    budget: float
    additional_notes: Optional[str] = None
