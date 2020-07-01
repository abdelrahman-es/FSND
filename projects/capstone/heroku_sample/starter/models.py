import os
from sqlalchemy import Column, String, create_engine, Integer, Date, Float
from flask_sqlalchemy import SQLAlchemy
import json

# database_name = "capstone"
# database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', database_name)
default_path = "postgres://saqmdnbucthosu:5e6ec82b00af5309ba7c19ccc534a2de33673b4fbe7304fbe467714e2be777d6@ec2-52-0-155-79.compute-1.amazonaws.com:5432/d3nuuppk8gou7m"
database_path = os.getenv('DATABASE_URL', default_path)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
# db.create_all()

# association table

Role = db.Table('Role', db.Model.metadata,
      db.Column('Movie_id', db.Integer, db.ForeignKey('movies.id')),
      db.Column('Actor_id', db.Integer, db.ForeignKey('actors.id')),
      db.Column('actor_role', db.String))

# Movie Class

class Movie(db.Model):
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)
  actors = db.relationship('Actor', secondary=Role, backref=db.backref('roles', lazy='joined'))

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date
    }

# Actor Class

class Actor(db.Model):
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'age': self.age,
      'gender': self.gender

    }
