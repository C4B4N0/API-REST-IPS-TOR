from fastapi import FastAPI, APIRouter, HTTPException
from views import ip_router
import requests

app = FastAPI()
router = APIRouter()

#@app.router.get('/tor')
#@app.get("/")
#def teste1():
#    return 'Olá mundo'

@router.get('/')
def teste():
    return 'Hello World!'

app.include_router(prefix='/teste', router=router)
app.include_router(ip_router)


# Endpoint 1: GET /tor-ips - Lista de IPs de saída do TOR
@app.get("/tor-ips", description="Obtém IPs de saída do TOR")
async def get_tor_ips():
    url = "https://check.torproject.org/torbulkexitlist"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            ips = response.text.strip().split("\n")
            return {"tor_ips": ips}
        else:
            raise HTTPException(
                status_code=500,
                detail=f"Falha ao obter IPs TOR. Status Code: {response.status_code}",
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na requisição: {str(e)}")