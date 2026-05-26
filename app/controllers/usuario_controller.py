from fastapi import APIRouter, HTTPException
from app.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioOut
from app.services import usuario_service

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", response_model=UsuarioOut, status_code=201)
def criar(dados: UsuarioCreate):
    try:
        return usuario_service.criar_usuario(dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[UsuarioOut])
def listar():
    return usuario_service.listar_usuarios()


@router.get("/{id_usuario}", response_model=UsuarioOut)
def buscar(id_usuario: int):
    usuario = usuario_service.buscar_usuario(id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


@router.put("/{id_usuario}", response_model=UsuarioOut)
def atualizar(id_usuario: int, dados: UsuarioUpdate):
    try:
        atualizado = usuario_service.atualizar_usuario(id_usuario, dados)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not atualizado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado ou sem campos para atualizar")
    return atualizado


@router.delete("/{id_usuario}", status_code=204)
def deletar(id_usuario: int):
    deletado = usuario_service.deletar_usuario(id_usuario)
    if not deletado:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")