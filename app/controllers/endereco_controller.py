from fastapi import APIRouter, HTTPException
from app.schemas.endereco_schema import EnderecoCreate, EnderecoUpdate, EnderecoOut
from app.services import endereco_service

router = APIRouter(prefix="/enderecos", tags=["Endereços"])


@router.post("/", response_model=EnderecoOut, status_code=201)
def criar(dados: EnderecoCreate):
    try:
        return endereco_service.criar_endereco(dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[EnderecoOut])
def listar():
    return endereco_service.listar_enderecos()


@router.get("/usuario/{id_usuario}", response_model=list[EnderecoOut])
def por_usuario(id_usuario: int):
    return endereco_service.enderecos_por_usuario(id_usuario)


@router.get("/{id_endereco}", response_model=EnderecoOut)
def buscar(id_endereco: int):
    endereco = endereco_service.buscar_endereco(id_endereco)
    if not endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return endereco


@router.put("/{id_endereco}", response_model=EnderecoOut)
def atualizar(id_endereco: int, dados: EnderecoUpdate):
    try:
        atualizado = endereco_service.atualizar_endereco(id_endereco, dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not atualizado:
        raise HTTPException(status_code=404, detail="Endereço não encontrado ou sem campos para atualizar")
    return atualizado


@router.delete("/{id_endereco}", status_code=204)
def deletar(id_endereco: int):
    deletado = endereco_service.deletar_endereco(id_endereco)
    if not deletado:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")