from app.database.supabase import get_supabase_client
from app.schemas.invoice_item_schema import InvoiceItemCreate, InvoiceItemUpdate

class InvoiceItemRepository:
    
    @staticmethod
    def create(invoice_item: InvoiceItemCreate):
        supabase = get_supabase_client()
        data = invoice_item.model_dump()
        result = supabase.table("invoice_items").insert(data).execute()
        return result.data[0]
    
    @staticmethod
    def get_all():
        supabase = get_supabase_client()
        result = supabase.table("invoice_items").select("*").execute()
        return result.data
    
    @staticmethod
    def get_by_id(invoice_item_id: int):
        supabase = get_supabase_client()
        result = supabase.table("invoice_items").select("*").eq("id", invoice_item_id).execute()
        return result.data[0] if result.data else None
    
    @staticmethod
    def update(invoice_item_id: int, invoice_item: InvoiceItemUpdate):
        supabase = get_supabase_client()
        data = invoice_item.model_dump(exclude_unset=True)
        result = supabase.table("invoice_items").update(data).eq("id", invoice_item_id).execute()
        return result.data[0]
    
    @staticmethod
    def delete(invoice_item_id: int):
        supabase = get_supabase_client()
        supabase.table("invoice_items").delete().eq("id", invoice_item_id).execute()
        return True