from fastapi import Depends
from strawberry.fastapi import BaseContext

from infrastructure.mysql.database import get_session
from infrastructure.user.user_repository import UserRepository
from usecases.user.fetch_user_by_id_usecase import FetchUserByIdUsecase


def init_user_repository(session=Depends(get_session)):
    return UserRepository(session)


def init_fetch_user_by_id_usecase(
    user_repository: UserRepository = Depends(init_user_repository),
):
    return FetchUserByIdUsecase(user_repository)


class UserContext(BaseContext):
    def __init__(self, fetch_user_by_id_usecase: FetchUserByIdUsecase):
        self.__fetch_user_by_id_usecase: FetchUserByIdUsecase = (
            fetch_user_by_id_usecase
        )

    def get_fetch_user_by_id_usecase(self):
        return self.__fetch_user_by_id_usecase


async def get_context(
    fetch_user_by_id_usecase: FetchUserByIdUsecase = Depends(
        init_fetch_user_by_id_usecase
    ),
) -> UserContext:
    return UserContext(fetch_user_by_id_usecase)
