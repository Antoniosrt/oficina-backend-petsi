from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import (
    usuario_controller,
    endereco_controller,
    categoria_controller,
    produto_controller,
    compra_controller,
    item_compra_controller,
)

app = FastAPI(
    title="Pet lojaa",
    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (ajuste conforme necessário)
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

app.include_router(usuario_controller.router)
app.include_router(endereco_controller.router)
app.include_router(categoria_controller.router)
app.include_router(produto_controller.router)
app.include_router(compra_controller.router)
app.include_router(item_compra_controller.router)


@app.get("/", tags=["Root"])
def root():
    return {"mensagem": "API rodando! Acesse /docs."}