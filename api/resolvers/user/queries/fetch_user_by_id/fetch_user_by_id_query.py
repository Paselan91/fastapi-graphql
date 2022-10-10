from strawberry.types import Info

from infrastructure.models.user_model import UserModel
from resolvers.user.queries.fetch_user_by_id.fetch_user_by_id_input import \
    FetchUserByIdInput


def fetch_user_by_id_query(info: Info, id: int) -> UserModel:
    input = FetchUserByIdInput(id)
    usecase = info.context.get_fetch_user_by_id_usecase()
    user_model = usecase.exec(input)

    return user_model
