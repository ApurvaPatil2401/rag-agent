# pipeline/loader.py

import aiomysql
import asyncio
from fetcher import fetch_documents
from processor import process_documents

from datetime import datetime, timedelta

async def insert_documents(docs):
    conn = await aiomysql.connect(
        host="localhost",
        port=3306,
        user="Apurva1234",
        password="Apurva123",  # Replace with your actual password
        db="federal_data"
    )

    async with conn.cursor() as cur:
        for doc in docs:
            await cur.execute("""
                INSERT INTO federal_documents (title, doc_type, publication_date, president, summary)
                VALUES (%s, %s, %s, %s, %s)
            """, (doc["title"], doc["doc_type"], doc["publication_date"], doc["president"], doc["summary"]))

    await conn.commit()
    conn.close()
    print(f"✅ Inserted {len(docs)} records into MySQL")

async def run_pipeline():
    today = datetime.today()
    last_week = today - timedelta(days=7)
    raw_docs = await fetch_documents(last_week.strftime("%Y-%m-%d"), today.strftime("%Y-%m-%d"))
    cleaned_docs = process_documents(raw_docs)
    await insert_documents(cleaned_docs)

# Run it
if __name__ == "__main__":
    asyncio.run(run_pipeline())
