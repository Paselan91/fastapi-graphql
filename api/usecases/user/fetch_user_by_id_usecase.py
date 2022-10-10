from domain.user.entity.user_entity import UserEntity
from domain.user.repository.user_repository_interface import \
    UserRepositoryInterface
from resolvers.user.queries.fetch_user_by_id.fetch_user_by_id_input import \
    FetchUserByIdInput
from usecases.user.dto.user_dto import UserDto


class FetchUserByIdUsecase:

    user_repository: UserRepositoryInterface

    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def exec(self, input: FetchUserByIdInput) -> UserEntity:
        user_entity = self.user_repository.find_by_id(input.get_id())
        return UserDto.to_model(user_entity)
