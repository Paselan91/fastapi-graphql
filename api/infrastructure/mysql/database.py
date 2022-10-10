from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from infrastructure.models.user_model import UserModel

# TODO: envから取得する
SQLALCHEMY_DATABASE_URL = "mysql://{user}:{password}@{host}/{db_name}?charset\
    =utf8".format(
    **{
        "user": "testuser",
        "password": "password",
        # hostはコンテナ名を指定する
        "host": "db",
        "db_name": "testdb",
    }
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding="utf-8", echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)
    create_user()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def create_user():
    session: Session = SessionLocal()
    user = UserModel()
    user.id = 1
    user.name = "田中　太郎"
    user.email = "hoge@test.com"
    session.add(user)
