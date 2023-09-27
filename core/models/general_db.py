from sqlalchemy import Table, Column, String, ForeignKey, MetaData, TIMESTAMP, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from uuid import uuid4
from config import DB_HOST, DB_NAME, DB_PORT, DB_PASS, DB_USER
# from core.cache.cache import RepositoryRedis

metadata = MetaData()

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
engine.connect()
# cache = RepositoryRedis()


class Base(DeclarativeBase):
    pass


class Menu(Base):
    __tablename__ = "menu"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(String)


class Submenu(Base):
    __tablename__ = "submenu"
    id = Column(String, primary_key=True)
    menu_id = Column(String, ForeignKey("menu.id"))
    title = Column(String)
    description = Column(String)


class Dishes(Base):
    __tablename__ = "dishes"
    id = Column(String, primary_key=True)
    submenu_id = Column(String, ForeignKey("submenu.id"))
    title = Column(String)
    description = Column(String)
    price = Column(String)


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine, autoflush=False)
session = Session()