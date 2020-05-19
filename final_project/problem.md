# Central de Erros
## Objetivos:
Em projetos modernos é cada vez mais comum o uso de arquiteturas baseadas em serviços ou microsserviços. Nestes ambientes complexos, erros podem surgir em diferentes camadas da aplicação (backend, frontend, mobile, desktop) e mesmo em serviços distintos. Desta forma, é muito importante que os desenvolvedores possam centralizar todos os registros de erros em um local, de onde podem monitorar e tomar decisões mais acertadas. Neste projeto vamos implementar um sistema para centralizar registros de erros de aplicações.<br>
A arquitetura do projeto é formada por:
## Backend - API:
1. Criar endpoints para serem usados pelo frontend da aplicação.
2. Criar um endpoint que será usado para gravar os logs de erro em um banco de dados relacional.
3. A API deve ser segura, permitindo acesso apenas com um token de autenticação válido.
## Frontend:
1. Deve implementar as funcionalidades apresentadas nos wireframes.
2. Deve ser acessada adequadamente tanto por navegadores desktop quanto mobile.
3. Deve consumir a API do produto.
4. Desenvolvida na forma de uma Single Page Application.
## Observações:
Se a aceleração tiver ênfase no backend (Java, Python, C#, Go, PHP, etc) a equipe deve obrigatoriamente implementar a API. A implementação do frontend não é necessária
Se a aceleração tiver ênfase em frontend (React, Vue, Angular, etc) a equipe deve obrigatoriamente implementar o frontend da aplicação e o backend pode ser substituido por uma aplicação mock. A implementação da API não é necessária, caso o time deseje podem ser utilizados mocks


