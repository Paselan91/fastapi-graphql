import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import Department as DepartmentModel, User as UserModel

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnections(relay.Connection):
    class Meta:
        node = User


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # デフォルトでは、ソートが有効化されている
    all_users = SQLAlchemyConnectionField(UserConnections)


schema = graphene.Schema(query=Query)
