from fastapi import FastAPI

from autenticacao import rotas_autenticacao
from fotografos import rotas_fotografos
from portifolios import rotas_portfolios


app = FastAPI()

app.include_router(rotas_autenticacao)
app.include_router(rotas_fotografos)
app.include_router(rotas_portfolios)

# uvicorn main:app --reload
# http://127.0.0.1:8000/docs
  

#endpoint:


