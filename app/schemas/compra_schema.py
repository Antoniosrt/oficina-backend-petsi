from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CompraCreate(BaseModel):
    id_usuario: int
    status: Optional[str] = "pendente"
    valor_total: Optional[float] = None


class CompraUpdate(BaseModel):
    status: Optional[str] = None
    valor_total: Optional[float] = None


class CompraOut(CompraCreate):
    id_compra: int
    data_compra: datetime