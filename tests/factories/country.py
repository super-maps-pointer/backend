# -*- encoding: utf-8 -*-
"""
Mock of Country table using factory_boy
"""
import factory

from app.models.country import Country


class CountryFactory(factory.Factory):
    class Meta:
        model = Country

    name = factory.Iterator(["France", "Italy", "Spain"])
    capital = factory.Iterator(["Paris", "Rome", "Madrid"])
