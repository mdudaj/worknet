# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - National Institute for Medical Research
"""

import os


class Config(object):
    """Base configuration"""

    db_user = os.environ.get('DB_USER', 'admin')
    db_password = os.environ.get('DB_PASSWORD', 's3cret@9653')
    db_name = os.environ.get('DB_NAME', 'worknet_dev')
    db_host = os.environ.get('DB_HOST', 'db')
    db_port = os.environ.get('DB_PORT', 5432)

    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'worknet_secret_key'
    DEBUG = False
    