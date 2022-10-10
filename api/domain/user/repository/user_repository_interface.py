from abc import ABC, abstractmethod
from typing import Optional

from domain.user.entity.user_entity import UserEntity


class UserRepositoryInterface(ABC):

    # @abstractmethod
    # def create(self, user_entity: UserEntity) -> Optional[UserEntity]:
    #     raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[UserEntity]:
        raise NotImplementedError

    # @abstractmethod
    # def update(self, user_entity: UserEntity) -> Optional[UserEntity]:
    #     raise NotImplementedError

    # @abstractmethod
    # def delete_by_id(self, id: str):
    #     raise NotImplementedError
