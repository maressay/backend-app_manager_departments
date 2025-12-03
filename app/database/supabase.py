from supabase import create_client, Client
from dotenv import load_dotenv
from typing import Optional
import os

load_dotenv()

SUPABSE_URL = os.getenv("SUPABASE_URL") 
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

_supabase: Optional[Client] = None

def get_supabase_client() -> Client:
    """
        Retorna una clase singleton de supabase para interactuar con la base de datos.
        Se crea una sola vez para evitar múltiples conexiones innecesarias.
    """
    
    global _supabase
    
    if SUPABASE_API_KEY is None or SUPABSE_URL is None:
        raise ValueError("Supabase URL or API Key is not set in environment variables.")
    
    if _supabase is None:
        _supabase = create_client(SUPABSE_URL, SUPABASE_API_KEY)
        
    return _supabase