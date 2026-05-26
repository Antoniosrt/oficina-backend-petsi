from fastapi import APIRouter, HTTPException
from app.schemas.categoria_schema import CategoriaCreate, CategoriaUpdate, CategoriaOut
from app.services import categoria_service

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.post("/", response_model=CategoriaOut, status_code=201)
def criar(dados: CategoriaCreate):
    try:
        return categoria_service.criar_categoria(dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[CategoriaOut])
def listar():
    return categoria_service.listar_categorias()


@router.get("/{id_categoria}", response_model=CategoriaOut)
def buscar(id_categoria: int):
    categoria = categoria_service.buscar_categoria(id_categoria)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria


@router.put("/{id_categoria}", response_model=CategoriaOut)
def atualizar(id_categoria: int, dados: CategoriaUpdate):
    try:
        atualizado = categoria_service.atualizar_categoria(id_categoria, dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not atualizado:
        raise HTTPException(status_code=404, detail="Categoria não encontrada ou sem campos para atualizar")
    return atualizado


@router.delete("/{id_categoria}", status_code=204)
def deletar(id_categoria: int):
    deletado = categoria_service.deletar_categoria(id_categoria)
    if not deletado:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")