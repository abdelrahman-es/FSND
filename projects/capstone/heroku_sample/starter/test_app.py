import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie
from datetime import date
from sqlalchemy import desc


class AgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        #self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', self.database_name)
        self.database_path = "postgres://saqmdnbucthosu:5e6ec82b00af5309ba7c19ccc534a2de33673b4fbe7304fbe467714e2be777d6@ec2-52-0-155-79.compute-1.amazonaws.com:5432/d3nuuppk8gou7m"
        setup_db(self.app, self.database_path)

        
        
        self.Casting_Assistant ={
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3c0pYbzBrYVM2RmV1LXdCU3hwRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWJkZWwuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjlkZTY3YWI1ZDhjMDAxOWNhNDEwYyIsImF1ZCI6ImNhcCIsImlhdCI6MTU5MzUyNjYwMywiZXhwIjoxNTkzNTMzODAzLCJhenAiOiJtZEE3dEdTNHNSNmhPVVMwdDBpQlJPczJmc2NIRGdVdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.nkU5qHazJ0GV7D6WRdEg8sbvSD3ydlgItJjXZnkz25aS63RNTX0400Cx7vrKi3DNXTd6OQyWXy57J9dQm5zKOW-Bqw8-0z2NRHaClq6g2pRLlzubBjUVSsU2wZiEZqsuGp1NkVjmKy2bZfdDGfGtDa8Wj4c_zO7tkrPt1T6FA6iFATsQTicExybWSKMZt7XbTl9LKRh3kqvAjKN6eLQo-4WmMlBoSe_EzXRGT6kzmhnPMDjnIG8yD2OT6hOPp3MBNqJpzZlQ69t9pYtsjYYBJUO_cvZq9kR9VaQypwhYKkgtp7N1CTAkRdGkvgBfgD0lBs51eH9Gx1WauWtJs_pGeQ'
        }

        self.Casting_Director ={
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3c0pYbzBrYVM2RmV1LXdCU3hwRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWJkZWwuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjlkYmY3ZDU4ZWEwMDAxOTMyZDcwMyIsImF1ZCI6ImNhcCIsImlhdCI6MTU5MzUyMjI5OSwiZXhwIjoxNTkzNTI5NDk5LCJhenAiOiJtZEE3dEdTNHNSNmhPVVMwdDBpQlJPczJmc2NIRGdVdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9ycyIsImRlbGV0ZTphY3RvcnMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.sQMlI_-KBCDf1POMIgO7TxUGe0hUJJ7xq_rex40br1iw8D7axeSuqn7gXALnBcTNzWPIKWLKVlEWu-Nddie8MMpMzcatfHgmmtGQ9jrg7WgWo04dlqH5TmW6Mc4ptBOyKYKYIMO6CtHX3QVTickyETdCK83rZ_4pKalosY4ivcfsL-eAzvBBEy0JIZsDipZPsDDf0M-7B3rAp0b5NGpYSs2sXSDRlmaEI55J4hYmCu3fvdoo7_nXkqlTzX0mToU_h1-kVsNyrIAf3T3knaRQ6MiJhSTsBw0OlYOEixr3KKpcPIJELr3VRsqwVCdgfXlXBUd60HGpc8DJB0ZJ4KpYOA'
        }

        self.Executive_Producer ={
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3c0pYbzBrYVM2RmV1LXdCU3hwRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWJkZWwuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEwNjc1NDIxNzg5NTg0MjMzNjYwIiwiYXVkIjpbImNhcCIsImh0dHBzOi8vZnNuZC1hYmRlbC5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNTkzNTIyODExLCJleHAiOjE1OTM1MzAwMTEsImF6cCI6Im1kQTd0R1M0c1I2aE9VUzB0MGlCUk9zMmZzY0hEZ1V0Iiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJjcmVhdGU6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJlZGl0OmFjdG9ycyIsImVkaXQ6bW92aWVzIiwicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.uihRdV3VCMa2MPgl25i4hqr0jvnvVZDHunlcz6sTr6AsaGKXcIwTu3R_rdfpiBqfb-DTxUeBTzDaXQuqwdNktX9QVlWQWBL2cYmK-Qr1nnQqzKL1SX-AQ69604dv5i51PWmLObmosO2TkFQy1Xlvd1iOaRroJ3ndKjSYfZk05Pm1wqmh46_DFK4LlGXf7hTZPim3xBptFt1bXUyjEKZtDMLVnnziLc_HQEYPx5hgf4L45KhZy15u3pVfZTvKYVfWpH3rs_5s4AEX1NDnuoatCr9XhpTV1Xsa8ecmfCnDhv0cY4KJgwcVLF90yC-VJyWkrtsf2X1BPwmImZEnkeyfZg'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint
    At least two tests of RBAC for each role
    """
    # [ROLE] / Executive_Producer
    # all permissions 
    # all below scenarios with Executive_Producer except last 4 scenarios 

    # [GET] /actors
    # one test success and one test error for endpoint 
    def test_get_all_actors(self):
        res = self.client().get('/actors', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_error_get_all_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permissions not found')

    def test_error_with_pages_get_actors(self):
        res = self.client().get('/actors?page=100000', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Resource Not Found')    
    
    # [GET] /movies
    # one test success and one test error for endpoint 
    def test_get_all_movies(self):
        res = self.client().get('/movies', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) > 0)

    def test_error_get_all_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permissions not found')

    def test_error_with_pages_get_movies(self):
        res = self.client().get('/movies?page=100000', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'] , 'Resource Not Found') 

    # [POST] /actors
    # one test success and one test error for endpoint      
    def test_post_actors(self):
        json_actors = {
            'name' : 'mohamed',
            'gender' : 'male',
            'age' : 25    
        } 
        res = self.client().post('/actors',json =json_actors, headers =self.Executive_Producer)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['success'], True)
        self.assertTrue(len(res.get_json()['actors']))

    def test_error_post_actors(self):
        json_actors = {
            'name' : 'mohamed'
        } 
        res = self.client().post('/actors', json = json_actors, headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)

    # [POST] /movies
    # one test success and one test error for endpoint   

    def test_post_movies(self):
        json_movies = {
            'title' : 'drama',
            'release_date' : '2020/02/20'   
        } 
        res = self.client().post('/movies',json =json_movies, headers =self.Executive_Producer)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['success'], True)
        self.assertTrue(len(res.get_json()['movies']))

    def test_error_post_movies(self):
        json_movies = {
            'title' : 'drama'
        } 
        res = self.client().post('/movies', json = json_movies, headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)  

    # [PATCH] /actors
    # one test success and one test error for endpoint  
    
    def test_patch_actors(self):
        json_actors = {
            'name' : 'Ali'   
        } 
        res = self.client().patch('/actors/2',json =json_actors, headers =self.Executive_Producer)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['success'], True)
        self.assertTrue(len(res.get_json()['actor']))

    def test_error_patch_actors(self):
        json_actors = {
            'name' : 'mohamed'
        } 
        res = self.client().patch('/actors/10000', json = json_actors, headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    # [PATCH] /movies
    # one test success and one test error for endpoint     
    
    def test_patch_movies(self):
        json_movies = {
            'title' : 'thing'   
        } 
        res = self.client().patch('/movies/2',json =json_movies, headers =self.Executive_Producer)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['success'], True)
        self.assertTrue(len(res.get_json()['movie']))

    def test_error_patch_movies(self):
        json_movies = {
            'title' : 'thing'
        } 
        res = self.client().patch('/movies/10000', json = json_movies, headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # [DELETE] /actors
    # one test success and one test error for endpoint  
    def test_delete_actors(self):
        res = self.client().delete('/actors/4', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], 4)

    def test_error_delete_actors(self):
        res = self.client().delete('/actors/1000', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    # [DELETE] /movies
    # one test success and one test error for endpoint  

    def test_delete_movies(self):
        res = self.client().delete('/movies/4', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], 4)

    def test_error_delete_movies(self):
        res = self.client().delete('/movies/1000', headers =self.Executive_Producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)  

    # [ROLE] / Casting_Assistant
    # just can read actors and movies
    # two tests
    
    def test_get_all_actors_with_Role(self):
        res = self.client().get('/actors', headers =self.Casting_Assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

    def test_delete_actors_with_Role(self):
        res = self.client().delete('/actors/5', headers =self.Casting_Assistant)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')

    # [ROLE] / Casting_Director
    # Add or delete an actor from the database and Modify actors or movies
    # two tests 

    def test_post_actors_with_Role(self):
        json_actors = {
            'name' : 'mohamed',
            'gender' : 'male',
            'age' : 25    
        } 
        res = self.client().post('/actors',json =json_actors, headers =self.Casting_Director)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json()['success'], True)
        self.assertTrue(len(res.get_json()['actors']))  

    def test_delete_movies_with_Role(self):
        res = self.client().delete('/movies/6', headers =self.Casting_Director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Permission not found.')  
      

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()