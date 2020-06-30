Capstone Project for FSND Full Stack Developer Nanodegree

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


#### Database Setup

 
for my local postgres path :"postgres://{}:{}@{}/{}".format(
   'postgres', 'postgres', 'localhost:5432', capstone" 
for my postgres on heroku :
"postgres://saqmdnbucthosu:5e6ec82b00af5309ba7c19ccc534a2de33673b4fbe7304fbe467714e2be777d6@ec2-52-0-155-79.compute-1.amazonaws.com:5432/d3nuuppk8gou7m"

change with your database path in brackets below
database_path = "postgres://{}:{}@{}/{}".format(<user-name>,'<password>','localhost:5432', <database_name>)"

## Running the server

From within the `starter` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### Tasks

## Endpoints and error handlung
Creating company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for actors and movies 
3. Create an endpoint to DELETE actors and movies using their ID. 
4. Create an endpoint to POST a new actor and new movie
5. Create a PATCH endpoint to patch actors and movies based on their IDs. 
6. Create error handlers for all expected errors including 400, 404, 422 and 405.

### Setup Auth0

1. Create a new, single page web application
2. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
3. Create new API permissions:
    -read:actors	
    -read:movies
    -delete:movies
    -delete:actors
    -create:movies
    -create:actors
    -edit:movies
    -edit:actors		

4. Create new roles for:
    - Casting Assistant
         -read:actors	
         -read:movies
    - Casting Director
        -read:actors	
        -read:movies
        -delete:actors
        -create:actors
        -edit:movies
        -edit:actors
    - Executive Producer   	
        can perform all actions

5. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 3 users
    - Sign into each account and make note of the JWT.
    - add your token in authorization tab 
    - for test cases you can just add to your endpoint a header with 
      " Bearer ......(your noted token)"



### End Points

GET /actors
Using Postman with sample below and curl
Sample: https://abdelrahmanproj.herokuapp.com/actors

   {
    "actors": [
        {
            "age": 30,
            "gender": "male",
            "id": 1,
            "name": "Mohamed"
        }
    ],
    "success": true
}
GET /movies
Using Postman with sample below
Sample: https://abdelrahmanproj.herokuapp.com/movies

   {
    "movies": [
        {
            "id": 1,
            "release_date": "Mon, 12 Oct 2020 00:00:00 GMT",
            "title": "comedy"
        }
    ],
    "success": true
}

DELETE /actors/actor_id
Using Postman with sample below
Sample: https://abdelrahmanproj.herokuapp.com/actors/2

    {
    "deleted": 2,
    "success": true
}

DELETE /movies/movie_id
Using Postman with sample below
Sample: https://abdelrahmanproj.herokuapp.com/actors/1

  {
    "deleted": 1,
    "success": true
}


POST /actors
Using Postman with sample below
Sample: https://abdelrahmanproj.herokuapp.com/actors

    {
    "actor_id": 3,
    "actors": {
        "age": 22,
        "gender": "female",
        "name": "Mary"
    },
    "success": true
}

POST /movies
Using Postman with sample below
Sample: https://abdelrahmanproj.herokuapp.com/movies

    {
    "movie_id": 1,
    "movies": {
        "release_date": "2020-10-12",
        "title ": "comedy"
    },
    "success": true
}

PATCH /actors/actor_id
Using Postman with sample below
Sample: https://abdelrahmanproj.herokuapp.com/actors/3

    {
    "actor": [
        {
            "age": 27,
            "gender": "female",
            "id": 3,
            "name": "Mary"
        }
    ],
    "success": true,
    "updated": 3
}
PATCH /movies/movie_id
Using Postman with sample below
Sample: https://abdelrahmanproj.herokuapp.com/movies/1

    {
    "movie": [
        {
            "id": 1,
            "release_date": "Mon, 12 Oct 2020 00:00:00 GMT",
            "title": "action"
        }
    ],
    "success": true,
    "updated": 1
}

### Unit tests 
to run test cases
use this command 
$ python test_app.py
.........................
----------------------------------------------------------------------
Ran 22 tests in 26.342s

OK