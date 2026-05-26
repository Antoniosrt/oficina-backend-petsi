from pydantic import BaseModel
from typing import Optional


class CategoriaCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None


class CategoriaUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None


class CategoriaOut(CategoriaCreate):
    id_categoria: int