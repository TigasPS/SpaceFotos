# SpaceFotos

> Uma plataforma criada para conectar fotógrafos e clientes em um único espaço.

## Sobre o projeto

O SpaceFotos é uma plataforma voltada para o universo da fotografia e da produção audiovisual.

A proposta é criar um ambiente onde fotógrafos possam apresentar seus trabalhos, construir seus portfólios, encontrar outros profissionais, participar de comunidades, divulgar eventos e negociar equipamentos.

Obs: Creio que o projeto que mentalizei seja extremamente complexo para meu nivel, sendo assim, creio que se esse projeto ter por objetivo criar de fato nossa proposta, gostaria de fazer uma vercao simplificada do projeto.

---

## Objetivos

O SpaceFotos busca:

* Dar visibilidade aos fotógrafos;
* Permitir a criação de perfis profissionais;
* Criar portfólios online;
* Facilitar o contato e o networking entre profissionais e clientes;
* Criar um sistema de avaliação e reputação;
* Permitir a criação e o cadastro de agências;
* Criar comunidades relacionadas aos nichos da fotografia;
* Possibilitar a comunicação entre usuários;
* Criar um espaço para compra e venda de equipamentos;
* Permitir a criação e divulgação de eventos;
* Permitir que clientes acessem a plataforma como visitantes e agendem eventos e trabalhos;
* Criar um sistema de avaliação dos fotógrafos por intermédio dos clientes;
* Utilizar métricas para destacar profissionais.

---

## Usuários

Cada usuário poderá possuir informações como:

```text
Usuário
├── ID
├── Nome
├── Username
├── Email
├── Senha
├── Foto de perfil
├── Biografia
├── Localização
├── Data de cadastro
├── Equipamentos
├── Agência
└── Reputação
```

O perfil poderá funcionar como uma apresentação profissional do fotógrafo.

---

## Portfólio

O principal recurso do SpaceFotos será o portfólio.

O usuário poderá:

* Adicionar fotografias;
* Criar álbuns;
* Organizar trabalhos;
* Adicionar descrições;
* Classificar trabalhos;
* Mostrar fotos antes e depois da edição;
* Compartilhar seu perfil.

---

## Sistema de avaliação

O SpaceFotos terá um sistema de avaliação para ajudar a construir a reputação dos profissionais.

A ideia é utilizar diferentes métricas para formar uma pontuação geral.

O cliente poderá avaliar o trabalho **somente se tiver realizado um evento ou trabalho concluído e agendado por meio da plataforma**.

Quanto melhores forem as avaliações, maior será a reputação do fotógrafo e, consequentemente, sua prioridade dentro da plataforma.

---

## 👥 Seguidores e networking

Os usuários poderão:

* Seguir fotógrafos;
* Acompanhar publicações;
* Encontrar profissionais;
* Criar conexões;
* Interagir com outros usuários.

O objetivo é transformar o SpaceFotos em uma rede profissional voltada para o audiovisual.

---

## 💬 Sistema de mensagens

Será planejado um sistema de comunicação entre usuários.

O sistema poderá futuramente permitir:

* Conversas individuais;
* Envio de mensagens;
* Compartilhamento de trabalhos;
* Contato profissional.

---

## 🏢 Agências

Profissionais poderão criar ou participar de agências.

Uma agência poderá apresentar:

```text
Agência
│
├── Nome
├── Descrição
├── Logo
├── Portfólio
│
└── Fotógrafos
    ├── Fotógrafo 1
    ├── Fotógrafo 2
    └── Fotógrafo 3
```

Isso permitirá que equipes de fotografia e audiovisual tenham uma presença conjunta dentro da plataforma.

---

## 👥 Comunidades

O SpaceFotos também terá comunidades.

Exemplos:

```text
📸 Fotografia de rua
🏟️ Fotografia esportiva
🎥 Videomakers
📷 Canon
📷 Sony
📷 Nikon
💡 Iluminação
🖥️ Edição
```

Os usuários poderão participar de comunidades relacionadas aos seus interesses e aos diferentes nichos da fotografia.

---

## 🛒 Marketplace

Uma área da plataforma será dedicada à compra e venda de equipamentos.

Exemplos:

* Câmeras;
* Lentes;
* Flash;
* Tripés;
* Cartões de memória;
* Acessórios;
* Equipamentos de vídeo.

A implementação deverá considerar mecanismos de segurança e proteção dos usuários.

---

## Eventos

Usuários poderão criar eventos relacionados à fotografia e ao audiovisual.

O organizador poderá visualizar os fotógrafos inscritos e, por meio da análise de seus portfólios, selecionar quais profissionais participarão do evento.

O processo poderá funcionar da seguinte forma:

```text
Organizador cria o evento
        ↓
Fotógrafos se inscrevem
        ↓
Organizador visualiza os inscritos
        ↓
Análise dos portfólios
        ↓
Seleção dos fotógrafos
        ↓
Participação no evento
```

---

## Banco de dados

O banco de dados será responsável por armazenar informações como:

* Usuários;
* Fotos;
* Álbuns;
* Seguidores;
* Mensagens;
* Comunidades;
* Agências;
* Eventos;
* Avaliações;
* Produtos.

O acesso ao banco de dados será realizado por meio da camada de persistência do backend.
