from domain.user.entity.user_entity import UserEntity
from infrastructure.models.user_model import UserModel


class UserDto:
    def to_model(user_entity: UserEntity) -> UserModel:
        user_model = UserModel()
        user_model.id = user_entity.get_id()
        user_model.name = user_entity.get_name().value
        user_model.email = user_entity.get_email().value
        user_model.created_at = user_entity.get_created_at()
        user_model.updated_at = user_entity.get_updated_at()
        return user_model
