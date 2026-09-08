from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker

from models import db, Usuario, Equipamento


rotas_autenticacao = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


# Dados necessários para cadastrar um usuário
class CadastroUsuario(BaseModel):
    nome: str
    username: str
    email: str
    telefone: str
    senha: str
    localizacao: str
    equipamentos: Equipamento
    data: str
    foto: str | None = None
    biografia: str | None = None
    agencia: str | None = None


# Endpoint de cadastro
@rotas_autenticacao.post("/cadastro")
async def cadastro(usuario: CadastroUsuario):

    Session = sessionmaker(bind=db)
    sessao = Session()

    novo_usuario = Usuario(
        nome=usuario.nome,
        username=usuario.username,
        email=usuario.email,
        telefone=usuario.telefone,
        senha=usuario.senha,
        localizacao=usuario.localizacao,
        equipamentos=usuario.equipamentos,
        data=usuario.data,
        foto=usuario.foto,
        biografia=usuario.biografia,
        agencia=usuario.agencia
    )

    sessao.add(novo_usuario)
    sessao.commit()
    sessao.refresh(novo_usuario)

    sessao.close()

    return {
        "mensagem": "Usuário cadastrado com sucesso!",
        "id": novo_usuario.id,
        "username": novo_usuario.username
    }

class LoginUsuario(BaseModel):
    username: str
    senha: str

# Endpoint de login
@rotas_autenticacao.post("/login")
async def login(usuario: LoginUsuario):

    Session = sessionmaker(bind=db)
    sessao = Session()

    usuario_encontrado = sessao.query(Usuario).filter(
        Usuario.username == usuario.username,
        Usuario.senha == usuario.senha
    ).first()

    sessao.close()

    if usuario_encontrado is None:
        return {
            "mensagem": "Usuário ou senha incorretos"
        }

    return {
        "mensagem": "Login realizado com sucesso!",
        "id": usuario_encontrado.id,
        "username": usuario_encontrado.username
    }

# Endpoint para consultar os dados do usuário
@rotas_autenticacao.get("/me")
async def meu_usuario(username: str):

    Session = sessionmaker(bind=db)
    sessao = Session()

    usuario = sessao.query(Usuario).filter(
        Usuario.username == username
    ).first()

    sessao.close()

    if usuario is None:
        return {
            "mensagem": "Usuário não encontrado"
        }

    return {
        "id": usuario.id,
        "nome": usuario.nome,
        "username": usuario.username,
        "email": usuario.email,
        "telefone": usuario.telefone,
        "localizacao": usuario.localizacao,
        "equipamentos": usuario.equipamentos.value,
        "foto": usuario.foto,
        "biografia": usuario.biografia,
        "agencia": usuario.agencia
    }