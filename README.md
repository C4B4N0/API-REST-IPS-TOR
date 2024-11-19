# DESAFIO - API REST - TOR

Este projeto tem por objetivo resolver o desafio proposto pelo Mercado Libre, que consiste no desenvolvimento de uma API REST que permita obter endereços IPs de redes TOR.

## FastAPI, PostgresQL, SQLAlchemy, Async Requests

### Dependências:
- Docker
- Docker-compose
- Python 3.9+
- Pipenv
- FastAPI
- uvicorn
- asyncpg
- aiohttp
- requests

### Como executar

Adicione o caminho do projeto na variável PYTHONPATH no arquivo ***.env***

Inicie o banco de dados postgres e o pgadmin:

``` 
sudo docker-compose up -d
```

Inicie o ambiente:

```
pipenv shell
```

Instalar as dependências usando o comando:

``` 
pipenv install
```

Inicie a aplicação:

```
unicorn main:app --port 8080
```
