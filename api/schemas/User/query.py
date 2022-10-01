import strawberry

from schemas.User import type


@strawberry.type
class UserQuery:
    @strawberry.field
    def fetchUser(self) -> type.User:
        return type.User(id=1, first_name="太郎", last_name="田中", email="test@test.com")
