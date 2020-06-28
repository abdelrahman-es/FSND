# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

GET '/actors'
Sample: curl http://127.0.0.1:5000/actors

{"actors":[{"age":26,
"gender":"male",
"id":1,
"name":"Abdelrahman"}],
"success":true}


```
GET /movies
General:

Sample: curl http://127.0.0.1:5000/movies

movies":[{"id":1,
"release_date":"Wed, 07 Oct 2020 00:00:00 GMT",
"title":"action"
}],
"success":true}



POST /actors

Sample: - curl -X POST http://127.0.0.1:5000/actors -H "Content-Type: application/json" -d '{"name": "Mohamed", "gender": "male", "age": 30}'

 {"actor_id":2,
 "actors":{
   "age":30,
   "gender":"male",
   "name":"Mohamed"
   },
   "success":true
   }

POST /movies

Sample: - curl -X POST http://127.0.0.1:5000/movies -H "Content-Type: application/json" -d '{"title": "comedy", "release_date": "2019/11/8"}'

 {"actor_id":2,
 "actors":{
   "age":30,
   "gender":"male",
   "name":"Mohamed"
   },
   "success":true
   }   

For using search 
Search: curl -X POST http://127.0.0.1:5000/questions/searchQuestions -H "Content-Type: application/json" -d '{"searchTerm": "what"}'
{
   "current_category": null,
  "questions": [
    {
      "answer": "Java",
      "category": "1",
      "difficulty": 5,
      "id": 17,
      "question": "what is your course"
    }
  ],
  "success": true,
  "total_questions": 1
}


POST /quizzes
General: - Returns success value and a random question object from the submitted category and doesn't belong to the previous questions list.

Sample:  curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [17, 18], "quiz_category": {"type": "Art", "id": "2"}}'

  "question": {
    "answer": "Linus Torvalds",
    "category": "2",
    "difficulty": 5,
    "id": 13,
    "question": "who created linux"
  },
  "success": true
}



DELETE /actors/{actor_id}

Sample: curl -X DELETE http://127.0.0.1:5000/actors/2

{
  "deleted": 2,
  "success": true
}

DELETE /movies/{movie_id}

Sample: curl -X DELETE http://127.0.0.1:5000/movies/1

{
  "deleted": 1,
  "success": true
}

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```