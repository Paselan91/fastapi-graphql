import strawberry
from strawberry.types import Info

from resolvers.user.queries.fetch_user_by_id.fetch_user_by_id_query import \
    fetch_user_by_id_query
from schemas.User.type import User as UserType


@strawberry.type
class UserQuery:
    @strawberry.field
    def fetchUser(self) -> UserType:
        return UserType(id=1, name="太郎", email="test@test.com")

    @strawberry.field(description="Get user by user's id")
    def fetchUserById(self, info: Info, id: int) -> UserType:
        return fetch_user_by_id_query(info, id)
