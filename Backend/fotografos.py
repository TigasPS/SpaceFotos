from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker

from models import db, Usuario, Portfolio


rotas_fotografos = APIRouter(
    prefix="/fotografos",
    tags=["Fotógrafos"]
)


# Endpoint para listar os fotógrafos
@rotas_fotografos.get("/")
async def listar_fotografos():

    Session = sessionmaker(bind=db)
    sessao = Session()

    fotografos = sessao.query(Usuario).filter(
        Usuario.ativo == True
    ).all()

    resultado = []

    for fotografo in fotografos:
        resultado.append({
            "id": fotografo.id,
            "nome": fotografo.nome,
            "username": fotografo.username,
            "localizacao": fotografo.localizacao,
            "equipamentos": fotografo.equipamentos.value,
            "foto": fotografo.foto,
            "biografia": fotografo.biografia,
            "agencia": fotografo.agencia
        })

    sessao.close()

    return resultado

# Endpoint para consultar um fotógrafo específico
@rotas_fotografos.get("/{username}")
async def buscar_fotografo(username: str):

    Session = sessionmaker(bind=db)
    sessao = Session()

    fotografo = sessao.query(Usuario).filter(
        Usuario.username == username,
        Usuario.ativo == True
    ).first()

    sessao.close()

    if fotografo is None:
        return {
            "mensagem": "Fotógrafo não encontrado"
        }

    return {
        "id": fotografo.id,
        "nome": fotografo.nome,
        "username": fotografo.username,
        "email": fotografo.email,
        "telefone": fotografo.telefone,
        "localizacao": fotografo.localizacao,
        "equipamentos": fotografo.equipamentos.value,
        "foto": fotografo.foto,
        "biografia": fotografo.biografia,
        "agencia": fotografo.agencia
    }

# Endpoint para listar o portfólio de um fotógrafo
@rotas_fotografos.get("/{username}/portfolio")
async def listar_portfolio(username: str):

    Session = sessionmaker(bind=db)
    sessao = Session()

    fotografo = sessao.query(Usuario).filter(
        Usuario.username == username,
        Usuario.ativo == True
    ).first()

    if fotografo is None:
        sessao.close()

        return {
            "mensagem": "Fotógrafo não encontrado"
        }

    portfolios = sessao.query(Portfolio).filter(
        Portfolio.usuario_id == fotografo.id,
        Portfolio.ativo == True,
        Portfolio.compartilhado == True
    ).all()

    resultado = []

    for portfolio in portfolios:
        resultado.append({
            "id": portfolio.id,
            "titulo": portfolio.titulo,
            "descricao": portfolio.descricao,
            "classificacao": (
                portfolio.classificacao.value
                if portfolio.classificacao else None
            ),
            "foto_antes": portfolio.foto_antes,
            "foto_depois": portfolio.foto_depois
        })

    sessao.close()

    return resultado