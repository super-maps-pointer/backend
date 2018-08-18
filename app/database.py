# -*- encoding: utf-8 -*-
"""
Utils functions to make manipulation with the postgresql database
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

url = os.environ.get('DATABASE_URL')
engine = create_engine(url)

if not database_exists(engine.url):
    create_database(engine.url)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.
    from app.models.country import Country, CountrySchema

    Base.metadata.create_all(bind=engine)
