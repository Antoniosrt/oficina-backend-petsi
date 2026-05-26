from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    telefone: Optional[str] = None

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    telefone: Optional[str] = None

class UsuarioOut(BaseModel):
    id_usuario: int
    nome: str
    email: str
    telefone: Optional[str]
    data_cadastro: datetime