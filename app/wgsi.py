# -*- encoding: utf-8 -*-
"""
File needed to start gunicorn server
"""
from app import create_app

app = create_app()
