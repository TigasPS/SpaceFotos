from fastapi import APIRouter

rotas_autenticacao = APIRouter(prefix= "/auth", tags=['Autenticação'] )

@rotas_autenticacao.get('/')
async def login():
    return {"mensagem": "Voce acessou a rota de LOGIN", "login": False}