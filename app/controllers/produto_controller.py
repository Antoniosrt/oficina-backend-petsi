from fastapi import APIRouter, HTTPException, Response
from app.services import produto_service
from app.schemas.produto_schema import ProdutoSchema

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.get("/", status_code=200)
def listar():
    return produto_service.listar_produtos()

@router.post("/", status_code=201)
def criar(produto: ProdutoSchema):
    return produto_service.criar(produto)

@router.put("/{id_produto}", status_code=200)
def atualizar(id_produto: int, produto: ProdutoSchema):
    atualizado = produto_service.atualizar(id_produto, produto)
    if not atualizado:
        raise HTTPException(status_code = 404, detail="Produto não encontrado")
    return atualizado

@router.delete("/{id_produto}")
def deletar (id_produto: int):
    existe = produto_service.deletar(id_produto)

    if not existe:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return Response(status_code = 204)

