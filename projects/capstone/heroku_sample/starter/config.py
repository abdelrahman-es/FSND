import os
SECRET_KEY = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres://saqmdnbucthosu:5e6ec82b00af5309ba7c19ccc534a2de33673b4fbe7304fbe467714e2be777d6@ec2-52-0-155-79.compute-1.amazonaws.com:5432/d3nuuppk8gou7m'
