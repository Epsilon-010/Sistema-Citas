from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker,declarative_base
import os


Base = declarative_base()

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost:5432/Sistemas"



engine = create_async_engine(DATABASE_URL,
                       pool_size=5,
                       max_overflow=10,
                       pool_recycle=1800,
                       pool_timeout=20,
                       )


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tablas creadas")


async def get_db():
    async with AsyncSessionLocal() as Session:
        yield Session
