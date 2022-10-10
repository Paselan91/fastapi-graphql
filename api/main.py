import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from contexts.user_contexts import get_context
from infrastructure.mysql.database import create_tables
from schemas.queries import Queries

# TODO: 機能していない tableできていない
create_tables()

schema = strawberry.Schema(query=Queries)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
