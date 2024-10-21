from abc import ABC, abstractmethod
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import selectinload

from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def create():
        raise NotImplementedError
    
    @abstractmethod
    async def get_all():
        raise NotImplementedError
    
    @abstractmethod
    async def get():
        raise NotImplementedError
    
    @abstractmethod
    async def update():
        raise NotImplementedError
    
    @abstractmethod
    async def delete():
        raise NotImplementedError
    

class SqlAlchemyRepository(AbstractRepository):
    model = None

    async def create(
            self, 
            data: dict
            ) -> dict:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    
    async def get_all(
            self, 
            offset: int = 0,
            limit: int = 10,
            *args,
            **kwargs
            ) -> list:
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row.to_read_model() for row in res.scalars().all()]
            return res
        
    async def get(
            self,
            *args,
            **kwargs
            ) -> dict:
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**kwargs)

            if args:
                stmt = stmt.options(*[selectinload(getattr(self.model, relation)) for relation in args])

            res = await session.execute(stmt)
            return res.scalar_one()

    async def update(
            self,
            data: dict,
            *args,
            **kwargs) -> bool:
        async with async_session_maker() as session:
            stmt = update(self.model).filter_by(**kwargs).values(**data)
            await session.execute(stmt)
            await session.commit()
            return True

    async def delete(
            self,
            *args,
            **kwargs):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(**kwargs)
            await session.execute(stmt)
            await session.commit()
            return True
    