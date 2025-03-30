# DESAFIO - API REST - TOR

Este projeto tem por objetivo desenvolver uma API REST que permita obter endereços IPs de redes TOR.

## FastAPI, PostgresQL, SQLAlchemy, Async Requests

### Dependências:
- Docker
- Docker-compose

### Como executar

Copiar arquivo de env

```
cp .env.sample .env
```

Inicie a aplicação e suas dependências

``` 
docker compose up --build -d
```

Instalação inicial do banco de dados:

```
docker compose run app python -m database.init_db
```
