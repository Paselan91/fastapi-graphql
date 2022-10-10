from datetime import datetime

from sqlalchemy import DATETIME, Column, String
from sqlalchemy.dialects.mysql import INTEGER as Integer
from sqlalchemy.ext.declarative import declarative_base

from domain.user.entity.user_entity import UserEntity

Base = declarative_base()


class UserModel(Base):

    __tablename__ = "users"

    id: int = Column(
        Integer(unsigned=True), primary_key=True, autoincrement=True
    )
    name: str = Column(String(255), nullable=False)
    email: str = Column(String(255), unique=True, nullable=False)
    created_at: datetime = Column(
        DATETIME, default=datetime.now, index=True, nullable=False
    )
    updated_at: datetime = Column(
        DATETIME, default=datetime.now, index=True, nullable=False
    )

    def to_entity(self) -> UserEntity:
        return UserEntity(
            id=self.id,
            name=self.name,
            email=self.email,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
