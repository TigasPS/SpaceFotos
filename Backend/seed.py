from sqlalchemy.orm import sessionmaker

from models import db, Usuario, Portfolio, Equipamento, Classificacao


Session = sessionmaker(bind=db)
sessao = Session()


usuario1 = Usuario(
    nome="Tiago Santos Pinheiro",
    username="tiags_ps",
    email="santospinheirotiago@gmail.com",
    telefone="79996562196",
    senha="12345678",
    localizacao="Aracaju - SE",
    equipamentos=Equipamento.SONY,
    data="2026-09-07"
)

usuario2 = Usuario(
    nome="João Silva",
    username="joaosilva",
    email="joao@email.com",
    telefone="79988888888",
    senha="123456",
    localizacao="Aracaju - SE",
    equipamentos=Equipamento.CANON,
    data="2026-09-07"
)


sessao.add(usuario1)
sessao.add(usuario2)

sessao.commit()


portfolio1 = Portfolio(
    usuario_id=usuario1.id,
    titulo="Fotografia Esportiva",
    descricao="Fotografias de eventos esportivos.",
    classificacao=Classificacao.ESPORTIVA,
    foto_antes="fotos/esportiva_antes.jpg",
    foto_depois="fotos/esportiva_depois.jpg",
    compartilhado=True,
    ativo=True

)

portfolio2 = Portfolio(
    usuario_id=usuario2.id,
    titulo="Retratos",
    descricao="Ensaio fotográfico de retratos.",
    classificacao=Classificacao.RETRATO,
    foto_antes="fotos/retrato_antes.jpg",
    foto_depois="fotos/retrato_depois.jpg",
    compartilhado=True,
    ativo=True
)


sessao.add(portfolio1)
sessao.add(portfolio2)

sessao.commit()

sessao.close()

print("Seed executada com sucesso!")