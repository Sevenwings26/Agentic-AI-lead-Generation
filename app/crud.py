from sqlalchemy.orm import Session
import models
from typing import Optional  # For optional fields

# create             
def fetch_leads(db: Session, full_name:str, email:str, phone_no:str, intent:str, property_type: str, location:str, budget:str, notes:Optional[str] = None) -> models.LeadContextTable:  # Added return type annotation
    try:
        new_lead = models.LeadContextTable(full_name=full_name, email=email, phone_no=phone_no, intent=intent, property_type=property_type, location=location, budget=budget, notes=notes)
        db.add(new_lead)
        db.commit()
        db.refresh(new_lead)
        return new_lead
    except Exception as e:
        db.rollback()
        raise ValueError(f"Lead creation failed: {str(e)}")