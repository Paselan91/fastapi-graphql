from datetime import datetime

from domain.user.value_object.email import Email
from domain.user.value_object.name import Name


class UserEntity:
    def __init__(
        self,
        id: int,
        name: Name,
        email: Email,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id: int = id
        self.name: Name = Name(name)
        self.email: Email = Email(email)
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, UserEntity):
            return self.id == o.id
        return False

    def get_id(self) -> int:
        return self.id

    def get_name(self) -> Name:
        return self.name

    def get_email(self) -> Email:
        return self.email

    def get_created_at(self) -> datetime:
        return self.created_at

    def get_updated_at(self) -> datetime:
        return self.updated_at
