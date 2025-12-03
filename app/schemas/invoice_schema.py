from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class InvoiceBase(BaseModel):
    contract_id: int
    invoce_date: date
    total_amount: float
    paid: bool = False
    paid_at: Optional[datetime] | None = None
    payment_method: Optional[str] | None = None
    created_at: datetime
    
class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    contract_id: int | None = None
    invoce_date: date | None = None
    total_amount: float | None = None
    paid: bool | None = None
    paid_at: datetime | None = None
    payment_method: str | None = None
    
class Invoice(BaseModel):
    id: int
    contract_id: int
    invoce_date: date
    total_amount: float
    paid: bool
    paid_at: datetime | None = None
    payment_method: str | None = None
    created_at: datetime