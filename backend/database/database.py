from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import create_engine

from config.settings import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    echo=False,
)


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session