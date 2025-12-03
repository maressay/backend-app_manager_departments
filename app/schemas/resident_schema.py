from pydantic import BaseModel
from datetime import datetime

class ResidentBase(BaseModel):
    dni: str
    name: str
    last_name: str
    phone_number: str | None = None
    
class ResidentCreate(ResidentBase):
    pass

class ResidentUpdate(BaseModel):
    dni: str | None = None
    name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    
class Resident(ResidentBase):
    dni: str
    name: str
    last_name: str
    phone_number: str | None = None
    created_at: datetime