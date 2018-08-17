# -*- encoding: utf-8 -*-
"""
Config file to import fixtures with pytest
"""
import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    return client
    # yield and then drop db
