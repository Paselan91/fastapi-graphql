from strawberry.tools import merge_types

from schemas.Post.query import PostQuery
from schemas.User.query import UserQuery

Queries = merge_types("Queries", (
        UserQuery,
        PostQuery
    )
)
