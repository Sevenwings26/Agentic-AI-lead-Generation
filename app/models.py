from sqlalchemy import Integer, Column, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class LeadContextTable(Base):
    __tablename__ = "lead_context_table"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_no = Column(String, nullable=True) # Optional
    intent = Column(String, nullable=False)
    property_type = Column(String, nullable=False)
    location = Column(String, nullable=False)
    budget = Column(Float, nullable=False)
    notes = Column(Text, nullable=True) # Optional
