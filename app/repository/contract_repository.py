from app.database.supabase import get_supabase_client
from app.schemas.contract_schema import ContractCreate, ContractUpdate

class ContractRepository:
    
    @staticmethod
    def create(contract: ContractCreate):
        supabase = get_supabase_client()
        data = contract.model_dump()
        result = supabase.table("contracts").insert(data).execute()
        return result.data[0]
    
    @staticmethod
    def get_all():
        supabase = get_supabase_client()
        result = supabase.table("contracts").select("*").execute()
        return result.data
    
    @staticmethod
    def get_by_id(contract_id: int):
        supabase = get_supabase_client()
        result = supabase.table("contracts").select("*").eq("id", contract_id).execute()
        return result.data[0] if result.data else None
    
    @staticmethod
    def update(contract_id: int, contract: ContractUpdate):
        supabase = get_supabase_client()
        data = contract.model_dump(exclude_unset=True)
        result = supabase.table("contracts").update(data).eq("id", contract_id).execute()
        return result.data[0]
    
    @staticmethod
    def delete(contract_id: int):
        supabase = get_supabase_client()
        supabase.table("contracts").delete().eq("id", contract_id).execute()
        return True