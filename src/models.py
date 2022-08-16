import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(12), unique=False, nullable=False)
    is_active = db.Column(Boolean(), unique=False, nullable=True)



    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }

class Character(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    homeworld = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250))
    skill = db.Column(db.String(250), nullable=False)
    

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "skill": self.skill
        }


class Planet(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    population = db.Column(db.String(250), nullable=True)
    diameter = db.Column(db.String(250), nullable=True)
    climate = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250))
   

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate
        }


class FavoriteTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    user = db.relationship('User')
    character_id = db.Column(db.Integer, ForeignKey('character.id'))
    character = db.relationship('Character')
    planet_id = db.Column(db.Integer, ForeignKey('planet.id'))
    planet = db.relationship('Planet')

    def __repr__(self):
        return '<FavoriteCharacter %r>' % self.id

    def serialize(self):
        user = User.query.get(self.id)
        return {
            "id": self.id
            
        }

