from pydantic import BaseModel
from datetime import datetime

class InvoiceItemBase(BaseModel):
    invoice_id: int
    description: str
    amount: float
    quantity: int
    total_price: float
    
class InvoiceItemCreate(InvoiceItemBase):
    pass

class InvoiceItemUpdate(BaseModel):
    invoice_id: int | None = None
    description: str | None = None
    amount: float | None = None
    quantity: int | None = None
    total_price: float | None = None
    
class InvoiceItem(BaseModel):
    id: int
    invoice_id: int
    description: str
    amount: float
    quantity: int
    total_price: float
    created_at: datetime