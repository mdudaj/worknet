# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - National Institute for Medical Research
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    db.init_app(app)

    return app