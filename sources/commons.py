
from httpx import AsyncClient


async def montferret_query(host: str, query: str, params: dict | None = None) -> dict:
    async with AsyncClient() as client:
        r = await client.post(host, json={
            "text": query,
            "params": params,
        })

        return r.json()
