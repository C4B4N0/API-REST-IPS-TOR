# DESAFIO - API REST - TOR

Este projeto tem por objetivo resolver o desafio proposto pelo Mercado Libre, que consiste no desenvolvimento de uma API REST que permita obter endereços IPs de redes TOR.

## FastAPI, PostgresQL, SQLAlchemy, Async Requests

### Dependências:
- Docker
- Docker-compose

### Como executar


Inicie a aplicação e suas dependências

``` 
docker compose up -d
```

Instalação inicial do banco de dados:

```
docker compose run app python -m database.init_db
```