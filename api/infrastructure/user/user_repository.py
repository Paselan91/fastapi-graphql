from typing import Optional

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from domain.user.entity.user_entity import UserEntity
from domain.user.repository.user_repository_interface import (
    UserRepositoryInterface,
)
from infrastructure.models.user_model import UserModel


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: int) -> Optional[UserEntity]:
        try:
            user = self.session.query(UserModel).filter_by(id=id).one()
        except NoResultFound:
            return None
        except Exception as e:
            raise e
        return user.to_entity()
