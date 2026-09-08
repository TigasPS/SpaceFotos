from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

from models import db, Portfolio, Classificacao


rotas_portfolios = APIRouter(
    prefix="/portfolios",
    tags=["Portfólios"]
)


class CadastroPortfolio(BaseModel):
    usuario_id: int
    titulo: str
    descricao: str | None = None
    classificacao: Classificacao | None = None
    foto_antes: str | None = None
    foto_depois: str | None = None
    compartilhado: bool = True


@rotas_portfolios.post("/")
async def cadastrar_portfolio(portfolio: CadastroPortfolio):

    Session = sessionmaker(bind=db)
    sessao = Session()

    novo_portfolio = Portfolio(
        usuario_id=portfolio.usuario_id,
        titulo=portfolio.titulo,
        descricao=portfolio.descricao,
        classificacao=portfolio.classificacao,
        foto_antes=portfolio.foto_antes,
        foto_depois=portfolio.foto_depois,
        compartilhado=portfolio.compartilhado
    )

    sessao.add(novo_portfolio)
    sessao.commit()
    sessao.refresh(novo_portfolio)

    sessao.close()

    return {
        "mensagem": "Portfólio cadastrado com sucesso!",
        "id": novo_portfolio.id,
        "titulo": novo_portfolio.titulo
    }
