
from httpx import AsyncClient, Timeout


async def montferret_query(host: str, query: str, params: dict | None = None) -> dict:
    timeout = Timeout(6.0, read=None)
    async with AsyncClient(timeout = timeout) as client:
        r = await client.post(host, json={
            "text": query,
            "params": params,
        })

        return r.json()
