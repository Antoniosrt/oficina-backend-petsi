from pydantic import BaseModel
from typing import Optional

class ProdutoSchema(BaseModel):
    # id_produto tem a categoria serial no banco de dados, o banco gera automaticamente
    id_categoria: Optional[int] = None
    nome: str
    descricao: Optional[str] = None
    preco: float
    estoque: int
    imagem_url: Optional[str] = None
    ativo: bool = True
    