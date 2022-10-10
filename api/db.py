from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

host = "db:3306"
db_name = "testdb"
user = "testuser"
password = "password"

DATABASE = "mysql://%s:%s@%s/%s?charset=utf8" % (
    user,
    password,
    host,
    db_name,
)

ENGINE = create_engine(DATABASE, encoding="utf-8", echo=True)

session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
)

Base = declarative_base()
Base.query = session.query_property()
