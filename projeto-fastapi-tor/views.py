from fastapi import APIRouter, HTTPException
from services import IpService
from schemas import AddIPInput, StandardOutput, ErrorOutput, IpListOutput
import requests

ip_router = APIRouter(prefix='/bancoIP')

#Endpoint POST que recebe um IP e envia para a base de dados
@ip_router.post('/create', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def ip_create(ip_input: AddIPInput):
    try:
        await IpService.add_ip(ip_address=ip_input.ip_address)
        return StandardOutput(message='Tudo certo!')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

#Endpoint extra que faz remoção de IP da base de dados   
@ip_router.delete('/delete/{ip_id}', description='My description', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def ip_delete(ip_id: int):
    try:
        await IpService.delete_ip(ip_id)
        return StandardOutput(message='Tudo certo!')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

#Endpoint GET que retorna uma consulta na base de dados
@ip_router.get('/list/', response_model=list[IpListOutput], responses={400: {'model': ErrorOutput}})
async def ip_list():
    try:
        return await IpService.list_ip()
        #return StandardOutput(message='Tudo certo!')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

#Endpoint GET que retorna os IPs da fonte externa, exceto aqueles bloqueados do banco de dados.    
@ip_router.get('/external-ips/', response_model=list[str], responses={400: {'model': ErrorOutput}})
async def get_external_ips():
    try:
        ips = await IpService.get_filtered_tor_ips()
        return ips
    except Exception as error:
        raise HTTPException(400, detail=str(error))