from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine('sqlite+aiosqlite:///./movie.db')
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()


async def get_db():
    async with async_session_maker() as session:
        yield session