from strawberry.types import Info

from infrastructure.models.user_model import UserModel
from resolvers.user.queries.fetch_user_by_id.fetch_user_by_id_input import \
    FetchUserByIdInput


class FetchUserByIdQuery:
    def exec(usecase, id: int) -> UserModel:
        input = FetchUserByIdInput(id)
        user_model = usecase.exec(input)

        return user_model
