from pydantic import BaseModel
from typing import Optional


class EnderecoCreate(BaseModel):
    id_usuario: int
    rua: str
    numero: Optional[str] = None
    bairro: Optional[str] = None
    cidade: str
    estado: str
    cep: Optional[str] = None


class EnderecoUpdate(BaseModel):
    rua: Optional[str] = None
    numero: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None


class EnderecoOut(EnderecoCreate):
    id_endereco: int