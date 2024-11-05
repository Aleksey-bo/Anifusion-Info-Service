from abc import ABC, abstractmethod
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError

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
        try:
            async with async_session_maker(expire_on_commit=False) as session:
                stmt = self.model(**data)
                session.add(stmt)
                await session.commit()
                await session.refresh(stmt)
                return stmt
        except SQLAlchemyError:
            return None

    async def get_all(
            self, 
            offset: int = 0,
            limit: int = 10,
            *args,
            **kwargs
            ) -> list:
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**kwargs)
            res = await session.execute(stmt)
            res = [await row.to_read_model() for row in res.scalars().all()]
            return res
        
    async def get(
            self,
            *args,
            **kwargs
            ):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(**kwargs)
            res = await session.execute(stmt)
            obj = res.scalars().first()
            return await obj.to_read_model()

    async def update(
            self,
            data: dict,
            *args,
            **kwargs) -> bool:
        try:
            async with async_session_maker() as session:
                stmt = await session.execute(select(self.model).filter_by(**kwargs))
                res = stmt.scalar_one_or_none()

                if not res: 
                    return False
                
                for key, value in data.items():
                    setattr(res, key, value)
                
                await session.commit()
                await session.refresh(res)
                return res
        except SQLAlchemyError as e:
            print(e)
            return None

    async def delete(
            self,
            *args,
            **kwargs):
        try:
            async with async_session_maker() as session:
                stmt = await session.execute(select(self.model).filter_by(**kwargs))
                res = stmt.scalar_one_or_none()

                if not res:
                    return False
                
                await session.delete(res)
                await session.commit()
                return True
        except SQLAlchemyError:
            return None
    