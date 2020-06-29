Capstone Project for FSND Full Stack Developer Nanodegree

End Points

GET /actors
Using Postman with sample below
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
