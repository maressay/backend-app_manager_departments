from app.database.supabase import get_supabase_client
from app.schemas.resident_schema import ResidentCreate, ResidentUpdate

class ResidentRepository:
    
    @staticmethod
    def create(resident: ResidentCreate):
        supabase = get_supabase_client()
        data = resident.model_dump()
        result = supabase.table("residents").insert(data).execute()
        return result.data[0]
    
    @staticmethod
    def get_all():
        supabase = get_supabase_client()
        result = supabase.table("residents").select("*").execute()
        return result.data
    
    @staticmethod
    def get_by_id(resident_id: int):
        supabase = get_supabase_client()
        result = supabase.table("residents").select("*").eq("id", resident_id).execute()
        return result.data[0] if result.data else None
    
    @staticmethod
    def update(resident_id: int, resident: ResidentUpdate):
        supabase = get_supabase_client()
        data = resident.model_dump(exclude_unset=True)
        result = supabase.table("residents").update(data).eq("id", resident_id).execute()
        return result.data[0]
    
    @staticmethod
    def delete(resident_id: int):
        supabase = get_supabase_client()
        supabase.table("residents").delete().eq("id", resident_id).execute()
        return True