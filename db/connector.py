import asyncio
import aiomysql

async def init_db():
    try:
        print("🔌 Connecting to MySQL...")
        conn = await aiomysql.connect(
            host="localhost",
            port=3306,
            user="Apurva1234",               # Change to your actual user
            password="Apurva123",  # Change to your password
            db="federal_data"
        )

        print("✅ Connected. Creating table...")

        async with conn.cursor() as cur:
            await cur.execute("""
            CREATE TABLE IF NOT EXISTS federal_documents (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title TEXT,
                doc_type VARCHAR(255),
                publication_date DATE,
                president VARCHAR(255),
                summary TEXT
            );
            """)
            print("✅ Table creation executed.")

        await conn.commit()
        conn.close()
        print("✅ Connection closed.")

    except Exception as e:
        print("❌ ERROR:", e)

if __name__ == "__main__":
    asyncio.run(init_db())
