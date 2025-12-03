from pydantic import BaseModel
from datetime import datetime

class DepartmentBase(BaseModel):
   name: str
   floor: int | None = None
   description: str | None = None
   
class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    name: str | None = None
    floor: int | None = None
    description: str | None = None
    
class Department(BaseModel):
    id: int
    name: str
    floor: int | None = None
    description: str | None = None
    created_ad: datetime
