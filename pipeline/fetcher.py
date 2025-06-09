# pipeline/fetcher.py

import aiohttp
import asyncio
from datetime import datetime, timedelta

BASE_URL = "https://www.federalregister.gov/api/v1/documents.json"

async def fetch_documents(start_date: str, end_date: str, limit=100):
    params = {
        "conditions[publication_date][gte]": start_date,
        "conditions[publication_date][lte]": end_date,
        "order": "newest",
        "per_page": limit
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL, params=params) as resp:
            data = await resp.json()
            return data.get("results", [])

# Test run
if __name__ == "__main__":
    async def test():
        end = datetime.today()
        start = end - timedelta(days=7)
        results = await fetch_documents(start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))
        print(f"Fetched {len(results)} documents.")

    asyncio.run(test())
