from fastapi import APIRouter, HTTPException
from app.schemas.compra_schema import CompraCreate, CompraUpdate, CompraOut
from app.services import compra_service

router = APIRouter(prefix="/compras", tags=["Compras"])


@router.post("/", response_model=CompraOut, status_code=201)
def criar(dados: CompraCreate):
    try:
        return compra_service.criar_compra(dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[CompraOut])
def listar():
    return compra_service.listar_compras()


@router.get("/usuario/{id_usuario}", response_model=list[CompraOut])
def por_usuario(id_usuario: int):
    return compra_service.compras_por_usuario(id_usuario)


@router.get("/{id_compra}", response_model=CompraOut)
def buscar(id_compra: int):
    compra = compra_service.buscar_compra(id_compra)
    if not compra:
        raise HTTPException(status_code=404, detail="Compra nao encontrada")
    return compra


@router.put("/{id_compra}", response_model=CompraOut)
def atualizar(id_compra: int, dados: CompraUpdate):
    try:
        atualizado = compra_service.atualizar_compra(id_compra, dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not atualizado:
        raise HTTPException(status_code=404, detail="Compra nao encontrada ou sem campos para atualizar")
    return atualizado


@router.delete("/{id_compra}", status_code=204)
def deletar(id_compra: int):
    deletado = compra_service.deletar_compra(id_compra)
    if not deletado:
        raise HTTPException(status_code=404, detail="Compra nao encontrada")
