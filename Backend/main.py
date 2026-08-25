from fastapi import FastAPI

app = FastAPI()

from Autenticacao import rotas_autenticacao

app.include_router(rotas_autenticacao)

# uvicorn main:app --reload
# http://127.0.0.1:8000
  

#endpoint:


