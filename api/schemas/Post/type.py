import strawberry


@strawberry.type
class Post:
    id: int
    title: str
    body: str
