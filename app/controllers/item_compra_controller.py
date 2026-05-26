from fastapi import APIRouter, HTTPException
from app.schemas.item_compra_schema import ItemCompraCreate, ItemCompraUpdate, ItemCompraOut
from app.services import item_compra_service

router = APIRouter(prefix="/itens-compra", tags=["Itens de Compra"])


@router.post("/", response_model=ItemCompraOut, status_code=201)
def criar(dados: ItemCompraCreate):
    try:
        return item_compra_service.criar_item(dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[ItemCompraOut])
def listar():
    return item_compra_service.listar_itens()


@router.get("/compra/{id_compra}", response_model=list[ItemCompraOut])
def por_compra(id_compra: int):
    return item_compra_service.itens_por_compra(id_compra)


@router.get("/{id_item_compra}", response_model=ItemCompraOut)
def buscar(id_item_compra: int):
    item = item_compra_service.buscar_item(id_item_compra)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item


@router.put("/{id_item_compra}", response_model=ItemCompraOut)
def atualizar(id_item_compra: int, dados: ItemCompraUpdate):
    try:
        atualizado = item_compra_service.atualizar_item(id_item_compra, dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not atualizado:
        raise HTTPException(status_code=404, detail="Item não encontrado ou sem campos para atualizar")
    return atualizado


@router.delete("/{id_item_compra}", status_code=204)
def deletar(id_item_compra: int):
    deletado = item_compra_service.deletar_item(id_item_compra)
    if not deletado:
        raise HTTPException(status_code=404, detail="Item não encontrado")