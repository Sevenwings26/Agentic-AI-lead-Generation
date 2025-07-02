from sqlalchemy import Integer, Column, String, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class LeadContextTable(Base):
    __tablename__ = "lead_context_table"
    # Inbound - from forms
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_no = Column(String, nullable=False)
    intent = Column(String, nullable=False)
    property_type = Column(String, nullable=False)
    location = Column(String, nullable=False)
    budget = Column(Float, nullable=False)
    notes = Column(Text, nullable=True) # Optional

    # improve table for scrapping leads (Outbound)
    lead_type = Column(String, default="inbound")
    score = Column(Integer, default=0)
    source_url = Column(String, nullable=True) # Optional
    created_at = Column(DateTime, default=datetime.utcnow)
