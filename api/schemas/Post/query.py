import strawberry

from schemas.Post import type


@strawberry.type
class PostQuery:
    @strawberry.field
    def fetchPost(self) -> type.Post:
        return type.Post(id=1, title="タイトルです", body="本文です。本文です。本文です。本文です。")
