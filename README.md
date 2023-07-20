# DESAFIO MURABEI

## Passo a Passo

### Backend

- Existe um arquivo [.env.example](01__backend/.env.example) com sugestões dos valores da variaveis de ambiente para rodar o projeto.
- A partir disso no mesmo direitorio deve se ter um arquivo `.env` com as mesmas variaveis
    - Obs.: APP_USER e APP_PASSWORD são as credenciais para login

- Após isso apenas rode o arquivo [build.sh](01__backend/build.sh) em seu diretorio raiz e ele irá criar as imagens e subir os container.
    - Obs.: lembra de atualizar o docker caso ele não reconheça o comando `docker compose`

### Frontend

- Existe um arquivo [next.config.js](02__frontend/codes/next.config.js) onde é necessario colocar a url a partir do host para o server.
    - Obs.: variavél chama `API_URL`

- Após isso apenas rode o arquivo [build.sh](02__frontend/build.sh) em seu diretorio raiz e ele irá criar as imagens e subir os container. Feito isso o frontend estará rodando no seguinte [url](http://localhost:3000/login)