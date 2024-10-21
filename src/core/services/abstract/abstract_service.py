from abc import ABC, abstractmethod


class AbstractService(ABC):
    @abstractmethod
    async def create_handler():
        pass

    @abstractmethod
    async def get_handler():
        pass

    @abstractmethod
    async def get_all_handler():
        pass

    @abstractmethod
    async def update_handler():
        pass

    @abstractmethod
    async def delete_handler():
        pass