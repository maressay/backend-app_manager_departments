from app.database.supabase import get_supabase_client
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate

class DepartmentRepository:
    
    @staticmethod
    def create(department: DepartmentCreate):
        supabase = get_supabase_client()
        data = department.model_dump()
        result = supabase.table("departments").insert(data).execute()
        return result.data[0]
    
    @staticmethod
    def get_all():
        supabase = get_supabase_client()
        result = supabase.table("departments").select("*").execute()
        return result.data
    
    @staticmethod
    def get_by_id(department_id: int):
        supabase = get_supabase_client()
        result = supabase.table("departments").select("*").eq("id", department_id).execute()
        return result.data[0] if result.data else None
    
    @staticmethod
    def update(department_id: int, department: DepartmentUpdate):
        supabase = get_supabase_client()
        data = department.model_dump(exclude_unset=True)
        result = supabase.table("departments").update(data).eq("id", department_id).execute()
        return result.data[0]
    
    @staticmethod
    def delete(department_id: int):
        supabase = get_supabase_client()
        supabase.table("departments").delete().eq("id", department_id).execute()
        return True