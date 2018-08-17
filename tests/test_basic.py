# -*- encoding: utf-8 -*-
"""
First test file
"""
import pytest
from flask import url_for


class TestMainPage(object):
    def test_index(self, client):
        res = client.get(url_for('index'))
        assert res.status_code == 200
