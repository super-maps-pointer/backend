# -*- encoding: utf-8 -*-
"""
Config file to import fixtures with pytest
"""
import pytest

from app import create_app
from app.database import db_session, Base, engine

from pytest_factoryboy import register
from tests.factories.country import CountryFactory
from sqlalchemy.orm import sessionmaker

# Register Factory to be used as fixture with pytest
register(CountryFactory)


@pytest.fixture(scope='session')
def testing_client(request):
    flask_app = create_app()
    testing_client = flask_app.test_client()
    yield testing_client

    # Drop all databases to start with a fresh one
    Base.metadata.drop_all(engine)


@pytest.fixture
def session(testing_client):
    session = db_session
    # establish  a SAVEPOINT just before beginning the test
    # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
    # begin_nested() may cause problems with some tests, if that it the case,
    # we need to drop this and recreate the whole database in between tests.
    session.begin_nested()
    yield session
    session.rollback()
