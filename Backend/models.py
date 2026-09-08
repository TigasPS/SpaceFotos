from enum import Enum as PyEnum
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, Enum
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db")
Base = declarative_base()

class Classificacao(PyEnum):
    RETRATO = "Retrato"
    ESPORTIVA = "Esportiva"
    CASAMENTO = "Casamento"
    EVENTOS = "Eventos"
    PRODUTOS = "Produtos"
    PAISAGEM = "Paisagem"

class Equipamento(PyEnum):
    CANON = "Canon"
    SONY = "Sony"
    NIKON = "Nikon"
    FUJIFILM = "Fujifilm"

#Usuário
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    nome = Column("Nome", String, nullable=False)
    username = Column("Nome de usuário", String, nullable=False, unique=True)
    email = Column("Email", String, nullable=False, unique=True)
    telefone = Column("Telefone", String, nullable=False)
    senha = Column("Senha", String, nullable=False)
    foto = Column("Foto", String, nullable=True)
    ativo = Column("Atividade", Boolean, default=True)
    biografia = Column("Bio", String, nullable=True)
    localizacao = Column("Localização", String, nullable=False)
    data = Column("Data", String, nullable=True)
    equipamentos = Column("Equipamentos", Enum(Equipamento), nullable=False)
    agencia = Column("Agencia", String, nullable=True)

    def __init__(
        self,
        nome,
        username,
        email,
        telefone,
        senha,
        localizacao,
        equipamentos,
        data,
        foto=None,
        biografia=None,
        agencia=None,
        ativo=True
    ):
        self.nome = nome
        self.username = username
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.localizacao = localizacao
        self.equipamentos = equipamentos
        self.foto = foto
        self.biografia = biografia
        self.data = data
        self.agencia = agencia
        self.ativo = ativo

# Portfolio
class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column("ID", Integer, primary_key=True, autoincrement=True)

    usuario_id = Column(
        "ID do Usuário",
        Integer,
        ForeignKey("usuarios.ID"),
        nullable=False
    )

    titulo = Column("Título", String, nullable=False)
    descricao = Column("Descrição", String, nullable=True)
    classificacao = Column("Classificação", Enum(Classificacao), nullable=True)
    foto_antes = Column("Foto Antes", String, nullable=True)
    foto_depois = Column("Foto Depois", String, nullable=True)
    compartilhado = Column("Compartilhado", Boolean, default=True)
    ativo = Column("Atividade", Boolean, default=True)

    def __init__(
        self,
        usuario_id,
        titulo,
        descricao=None,
        classificacao=None,
        foto_antes=None,
        foto_depois=None,
        compartilhado=True,
        ativo=True
    ):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descricao = descricao
        self.classificacao = classificacao
        self.foto_antes = foto_antes
        self.foto_depois = foto_depois
        self.compartilhado = compartilhado
        self.ativo = ativo