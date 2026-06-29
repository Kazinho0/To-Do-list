from pydantic import BaseModel , Field
from typing import Optional , List

class CreateTarefa(BaseModel):
    titulo: str = Field (..., max_length=50)
    descrição: Optional[str] = Field (..., max_length=500)

class ResponseTarefa(BaseModel):
    id: int
    titulo: str
    descrição: str
    estado: bool

    class Config:
        from_attributes = True