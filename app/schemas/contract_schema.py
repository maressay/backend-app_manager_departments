from pydantic import BaseModel
from datetime import date, datetime

class ContractBase(BaseModel):
    department_id: int
    resident_id: int
    start_date: date
    end_date: date | None = None
    status: str = "active"

class ContractCreate(ContractBase):
    pass

class ContractUpdate(BaseModel):
    department_id: int | None = None
    resident_id: int | None = None
    start_date: date | None = None
    end_date: date | None = None
    status: str | None = None
    
class Contract(BaseModel):
    id: int
    department_id: int
    resident_id: int
    start_date: date
    end_date: date | None = None
    status: str
    created_at: datetime