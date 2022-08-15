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
    # planet_favorites = relationship('FavoritePlanet', backref='User', lazy=True)
    # character_favorites = relationship('FavoriteCharacter', backref='User', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }

class Character(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    character_homeworld = db.Column(db.String(250), nullable=False)
    character_name = db.Column(db.String(250))
    character_skill = db.Column(db.String(250), nullable=False)
    

    def __repr__(self):
        return '<Character %r>' % self.character_name

    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "character_skill": self.character_skill
        }


class Planet(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    planet_population = db.Column(db.Integer, nullable=False)
    planet_diameter = db.Column(db.Integer, nullable=False)
    planet_climate = db.Column(db.String(250), nullable=False)
    planet_name = db.Column(db.String(250))
   

    def __repr__(self):
        return '<Planet %r>' % self.planet_name

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "planet_climate": self.planet_climate
        }


# class FavoriteCharacter(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, ForeignKey('user.id'))
#     character_id = db.Column(db.Integer, ForeignKey('character.character_id'))

#     def __repr__(self):
#         return '<FavoriteCharacter %r>' % self.user_id

#     def serialize(self):
#         user = User.query.get(self.user_id)
#         return {
#             "user": user.username,
#             "character_id": self.character_id,
#         }


# class FavoritePlanet(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # user_id = db.Column(db.Integer, ForeignKey('user.id'))
    # planet_id = db.Column(db.Integer, ForeignKey('planet.planet_id'))        

    # def __repr__(self):
    #     return '<FavoritePlanet %r>' % self.user_id

    # def serialize(self):
    #     user = User.query.get(self.user_id)
    #     return {
    #         "id": self.id,
    #         "user": user.username,
    #         "planet_id": self.planet_id,
    #     }