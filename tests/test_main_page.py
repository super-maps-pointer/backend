# -*- encoding: utf-8 -*-
"""
First test file
"""
import pytest

from flask import json


class TestMainPage(object):
    def test_index(self, testing_client):
        """ Test dummy hello world route """
        res = testing_client.get('/')
        assert res.status_code == 200

    def test_get_countries(self, testing_client, session, country):
        """ Add object to database to see if the function returns a json as expected

        Keyword arguments:
        testing_client -- flask app in test mode.
        session -- cleared after each functions.
        country -- Country object
        """

        # Add dummy data
        session.add(country)
        session.commit()

        res = testing_client.get('/countries')
        expected_data = json.loads(res.get_data())[0]

        assert res.status_code == 200
        assert expected_data['name'] == country.name

    def test_get_countries_dataless(self, testing_client):
        """ Test get country on empty database to see if its clear

        Keyword arguments:
        testing_client -- flask app in test mode.
        """
        res = testing_client.get('/countries')
        expected_data = json.loads(res.get_data())

        assert res.status_code == 200
        assert expected_data == []

    def test_post_countries(self, testing_client):
        """ Test get country on empty database to see if its clear

        Keyword arguments:
        testing_client -- flask app in test mode.
        """
        res = testing_client.post('/countries', json={
            'name': 'France', 'capital': 'Paris'
        })

        expected_data = json.loads(res.get_data())

        assert res.status_code == 201
        assert expected_data['name'] == 'France'
