# agent/tools.py

import aiomysql
import datetime

async def query_documents(president: str = None, start_date: str = None, end_date: str = None):
    conn = await aiomysql.connect(
        host="localhost",
        port=3306,
        user="Apurva1234",
        password="Apurva123",  # change this
        db="federal_data"
    )

    query = "SELECT title, publication_date, summary FROM federal_documents WHERE 1=1"
    args = []

    if president:
        query += " AND president LIKE %s"
        args.append(f"%{president}%")

    if start_date:
        query += " AND publication_date >= %s"
        args.append(start_date)

    if end_date:
        query += " AND publication_date <= %s"
        args.append(end_date)

    async with conn.cursor() as cur:
        await cur.execute(query, args)
        result = await cur.fetchall()

    await conn.ensure_closed()
    return [
        {"title": r[0], "date": str(r[1]), "summary": r[2][:300]}
        for r in result
    ]
