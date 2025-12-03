from app.database.supabase import get_supabase_client
from app.schemas.invoice_schema import InvoiceCreate, InvoiceUpdate


class InvoiceRepository:
    
    @staticmethod
    def create(invoice: InvoiceCreate):
        supabase = get_supabase_client()
        data = invoice.model_dump()
        result = supabase.table("invoices").insert(data).execute()
        return result.data[0]
    
    @staticmethod
    def get_all():
        supabase = get_supabase_client()
        result = supabase.table("invoices").select("*").execute()
        return result.data
    
    @staticmethod
    def get_by_id(invoice_id: int):
        supabase = get_supabase_client()
        result = supabase.table("invoices").select("*").eq("id", invoice_id).execute()
        return result.data[0] if result.data else None
    
    @staticmethod
    def update(invoice_id: int, invoice: InvoiceUpdate):
        supabase = get_supabase_client()
        data = invoice.model_dump(exclude_unset=True)
        result = supabase.table("invoices").update(data).eq("id", invoice_id).execute()
        return result.data[0]
    
    @staticmethod
    def delete(invoice_id: int):
        supabase = get_supabase_client()
        supabase.table("invoices").delete().eq("id", invoice_id).execute()
        return True