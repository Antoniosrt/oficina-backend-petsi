from pydantic import BaseModel
from typing import Optional


class ItemCompraCreate(BaseModel):
    id_compra: int
    id_produto: int
    quantidade: int
    preco_unitario: float
    subtotal: float


class ItemCompraUpdate(BaseModel):
    quantidade: Optional[int] = None
    preco_unitario: Optional[float] = None
    subtotal: Optional[float] = None


class ItemCompraOut(ItemCompraCreate):
    id_item_compra: int