from typing import Iterator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

# TODO: envから取得する
DB_URL = "mysql://{user}:{password}@{host}/{db_name}?charset=utf8".format(
    **{
        "user": "testuser",
        "password": "password",
        # hostはコンテナ名を指定する
        "host": "db",
        "db_name": "testdb",
    }
)

engine = create_engine(DB_URL, encoding="utf-8", echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
