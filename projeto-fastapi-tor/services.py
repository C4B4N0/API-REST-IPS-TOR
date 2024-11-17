from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete
from database.models import BancoIP
from database.connection import async_session
import requests



class IpService:
    async def add_ip(ip_address: str):
        async with async_session() as session:
            session.add(BancoIP(ip_address=ip_address))
            await session.commit()

    async def delete_ip(ip_id):
        async with async_session() as session:
            await session.execute(delete(BancoIP).where(BancoIP.id==ip_id))
            await session.commit()

    async def list_ip():
        async with async_session() as session:
            result = await session.execute(select(BancoIP))
            return result.scalars().all()

    async def get_tor_ips():
        """Busca IPs de saída do TOR da fonte externa."""
        url = "https://check.torproject.org/torbulkexitlist"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text.strip().split("\n")
            else:
                raise Exception(
                    f"Erro ao buscar IPs da fonte externa. Código: {response.status_code}"
                )
        except Exception as e:
            raise Exception(f"Erro na requisição externa: {str(e)}")
        
    async def get_filtered_tor_ips():
        """Retorna IPs externos filtrados pelo banco de dados."""
        tor_ips = await IpService.get_tor_ips()
        async with async_session() as session:
            # Busca todos os IPs bloqueados
            result = await session.execute(select(BancoIP.ip_address))
            blocked_ips = {row[0] for row in result.all()}  # Converte para set para eficiência

        # Filtra os IPs externos
        filtered_ips = [ip for ip in tor_ips if ip not in blocked_ips]
        return filtered_ips