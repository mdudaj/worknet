# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - National Institute for Medical Research
"""

from flask.cli import FlaskGroup

from api.app import create_app, db


app = create_app()

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    """Creates the database tables."""
    db.drop_all()
    db.create_all()
    db.session.commit()
