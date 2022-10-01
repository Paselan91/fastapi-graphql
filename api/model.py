from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from db import ENGINE, Base


# テーブル定義
class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(128), nullable=False)


# モデル定義
class User(BaseModel):
    id: int
    name: str
    email: str


def main():
    # テーブル構築
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
