# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - National Institute for Medical Research
"""

from api.app import db


class Catalogue(db.Model):
    __tablename__ = 'catalogue'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self,name,price,description,created_at,updated_at):
        self.name = name
        self.price = price
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f'<Catalogue {self.name}, Price: {self.price}>'
    

class Order(db.Model):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    catalogue_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self,customer_id,catalogue_id,status,created_at,updated_at):
        self.customer_id = customer_id
        self.catalogue_id = catalogue_id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f'<Order {self.customer_id}, Catalogue: {self.catalogue_id}>'