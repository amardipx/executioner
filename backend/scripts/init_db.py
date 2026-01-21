import asyncio

from app.db.pool import engine, Base
from app.models.domain import User  # <-- CRITICAL LINE

async def init():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init())
