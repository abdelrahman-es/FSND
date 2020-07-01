import os
from flask import Flask, request, abort, jsonify
from auth import AuthError, requires_auth
from flask_cors import CORS
import random
from models import setup_db, Actor, Movie, Role

RECORDS_PER_PAGE = 10

def paginate_outputs(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * RECORDS_PER_PAGE
    end = start + RECORDS_PER_PAGE

    objects = [object_name.format() for object_name in selection]
    current_objects = objects[start:end]

    return current_objects

def create_app(test_config=None):
  app = Flask(__name__)
  setup_db(app)
  '''
  @TODO: CORS
  '''
  CORS(app, resources={'/': {'origins': '*'}})
  '''
  @TODO:
  '''
  @app.after_request
  def after_request(response):
    '''
    Sets access control.
    '''
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  @app.route('/')
  def index():
    return jsonify({'message': 'Welcome'}
                   )
  '''
  @TODO: Get Actors .
  '''
  @app.route('/actors', methods=['GET'])
  @requires_auth('read:actors')
  def get_all_actors(token):
    actors = Actor.query.order_by(Actor.id).all()
    current_actors = paginate_outputs(request, actors)

    if len(current_actors) == 0:
        abort(404)
    return jsonify({
        'success': True,
        'actors': current_actors
    })

  '''
  @TODO: Get Movies .
  '''
  @app.route('/movies', methods=['GET'])
  @requires_auth('read:movies')
  def get_all_movies(token):
    movies = Movie.query.order_by(Movie.id).all()
    current_movies = paginate_outputs(request, movies)
    if len(current_movies) == 0:
        abort(404)

    return jsonify({
        'success': True,
        'movies': current_movies
    })
  '''
  @TODO:DELETE actor.
  '''
  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actors(token, actor_id):
    actor = Actor.query.filter(
        Actor.id == actor_id).one_or_none()
    if actor:
        try:
            actor.delete()

            return jsonify({
                'success': True,
                'deleted': actor_id
            })

        except Exception:
            abort(400)
    else:
        abort(404)

  '''
  @TODO:DELETE movie.
  '''
  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movies(token, movie_id):
    movie = Movie.query.filter(
        Movie.id == movie_id).one_or_none()
    if movie:
        try:
            movie.delete()

            return jsonify({
                'success': True,
                'deleted': movie_id
            })

        except Exception:
            abort(400)
    else:
        abort(404)
  '''
  @TODO: POST actor.
  '''
  @app.route('/actors', methods=['POST'])
  @requires_auth('create:actors')
  def add_actor(token):
    data = request.get_json()

    new_name = data.get('name', None)
    new_gender = data.get('gender', None)
    new_age = data.get('age', None)
    if not(new_name and new_gender and new_age):
        abort(400)
    try:
        actor = Actor(
                name=new_name,
                gender=new_gender,
                age=new_age
                )
        actor.insert()

        return jsonify({
                'success': True,
                'actor_id': actor.id,
                'actors': data
            })

    except Exception:
        abort(422)

  '''
  @TODO: POST movie.
  '''
  @app.route('/movies', methods=['POST'])
  @requires_auth('create:movies')
  def add_movie(token):
    data = request.get_json()

    new_title = data.get('title', None)
    new_release_date = data.get('release_date', None)

    if not(new_title and new_release_date):
        abort(400)

    try:
        movie = Movie(
                title = new_title,
                release_date = new_release_date)
        movie.insert()

        return jsonify({
                'success': True,
                'movie_id': movie.id,
                'movies': data
            })

    except Exception:
        abort(422)

  '''
  @TODO: PATCH actor.
  '''
  @app.route('/actors/<actor_id>', methods=['PATCH'])
  @requires_auth('edit:actors')
  def edit_actors(token, actor_id):

    body = request.get_json()

    if not body:
      abort(400)

    if not actor_id:
      abort(400)

    update_actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if not update_actor:
      abort(404)

    name = body.get('name', update_actor.name)
    age = body.get('age', update_actor.age)
    gender = body.get('gender', update_actor.gender)

    update_actor.name = name
    update_actor.age = age
    update_actor.gender = gender

    return jsonify({
      'success': True,
      'updated': update_actor.id,
      'actor': [update_actor.format()]
    })

  '''
  @TODO: PATCH movie.
  '''
  @app.route('/movies/<movie_id>', methods=['PATCH'])
  @requires_auth('edit:movies')
  def edit_movies(token, movie_id):

    body = request.get_json()
    if not body:
      abort(400)

    if not movie_id:
      abort(400)

    update_movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if not update_movie:
      abort(404)

    title = body.get('title', update_movie.title)
    release_date = body.get('release_date', update_movie.release_date)

    update_movie.title = title
    update_movie.release_date = release_date

    return jsonify({
      'success': True,
      'updated': update_movie.id,
      'movie': [update_movie.format()]
    })

  '''
  @TODO: Error handling.
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "Error": 404,
        "message": 'Resource Not Found'
    }), 404

  @app.errorhandler(422)
  def uprocessable(error):
    return jsonify({
        "success": False,
        "Error": 422,
        "message": 'unprocessable'
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
        "success": False,
        "Error": 400,
        "message": 'Bad request'
    }), 400

  @app.errorhandler(405)
  def not_allowed(error):
    return jsonify({
        "success": False,
        "Error": 405,
        "message": 'Method Not allowed'
    }), 405

  @app.errorhandler(500)
  def bad_request(error):
    return jsonify({
        "success": False,
        "Error": 500,
        "message": 'Internal Server Error'
    }), 500

  @app.errorhandler(AuthError)
  def authentification_failed(AuthError):
    return jsonify({
        "success": False,
        "error": AuthError.status_code,
        "message": AuthError.error['description']
    }), AuthError.status_code
  return app

app = create_app()

if __name__ == '__main__':
    app.run()