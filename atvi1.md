Atividade 1

1. Quais tabelas você definiu inicialmente?

Inicialmente foram definidas duas tabelas para o banco de dados: 
usuarios: responsável por armazenar os dados dos usuários/fotógrafos, como nome, username, e-mail, telefone, senha, localização, equipamentos, biografia e agência.
portfolios: responsável por armazenar os trabalhos dos fotógrafos, contendo informações como título, descrição, classificação e imagens antes/depois, além da relação com o usuário.

2. Você utilizou migrations? Se sim, quantas migrations? Descreva em uma frase o que cada uma faz.

Sim. Foi utilizada 1 migration, criada com o Alembic:
•	8637020c7fb3_initial_migration.py — cria a estrutura inicial das tabelas usuarios e portfolios no banco de dados.

3. Qual o caminho do arquivo que gera a seed do seu banco?
O arquivo responsável por gerar a seed do banco ?

está localizado em:
Backend/seed.py

4. Quais os endpoints que você irá implementar inicialmente?
Os endpoints definidos inicialmente são:

Método	Path
POST	/auth/cadastro
POST	/auth/login
GET	/auth/me
GET	/fotografos/
GET	/fotografos/{username}
GET	/fotografos/{username}/portfolio
POST	/portfolios/

Esses endpoints foram priorizados porque representam as principais funcionalidades iniciais do SpaceFotos. Primeiro, é necessário permitir que os usuários realizem cadastro e login e possam consultar seus próprios dados. Em seguida, a API precisa permitir a busca e visualização dos fotógrafos cadastrados, incluindo seus perfis e portfólios. Por fim, o cadastro de portfólios permite que os fotógrafos adicionem seus trabalhos à plataforma. Dessa forma, esses endpoints estabelecem a base para as principais funcionalidades da aplicação.

5. Você está usando algum framework para escrever os endpoints da sua API? Se sim, qual? 

Sim. Está sendo utilizado o FastAPI.
