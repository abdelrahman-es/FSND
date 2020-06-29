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
        self.database_path = "postgres://{}:{}@{}/{}".format(
        'postgres', 'postgres', 'localhost:5432', self.database_name)
        #self.database_path = "postgres://saqmdnbucthosu:5e6ec82b00af5309ba7c19ccc534a2de33673b4fbe7304fbe467714e2be777d6@ec2-52-0-155-79.compute-1.amazonaws.com:5432/d3nuuppk8gou7m"
        setup_db(self.app, self.database_path)

        
        
        self.producer_token ={
            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjZ3c0pYbzBrYVM2RmV1LXdCU3hwRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtYWJkZWwuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjlkZTY3YWI1ZDhjMDAxOWNhNDEwYyIsImF1ZCI6ImNhcCIsImlhdCI6MTU5MzQ1MDc1MiwiZXhwIjoxNTkzNDU3OTUyLCJhenAiOiJtZEE3dEdTNHNSNmhPVVMwdDBpQlJPczJmc2NIRGdVdCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsicmVhZDphY3RvcnMiLCJyZWFkOm1vdmllcyJdfQ.bnj0sg_6dw1DcWmR1YwcTefK0Wuyp_riyt_pQVFOQmBs3EdRMTDlvvAOuxBHSjjM2ei7bIaX1B5_z6rh2ZK_HHx6DxZQFWRAqSsG4Rmx3Cb44QhrfJ4SZQvvmk31liwy88wwQZqHDCGgVNQoYxw994WCgIZnMhrGRtuUI-e_uBZd4EFPUiUDvEuQJV8ykroaH7QIK2DbugYfLD9OO9E7lve47Mh-OkW58FUNQL2r8fIlkYpTlKbjnrSG1k_Yct6-qxWbKC_7L4_BIFRhkUI-6d8SPQ92Qy7GaXoP4Ri14xyBRXwVOoSXmkeb4kTWCZedUU-nj3YFdYFFuFIClu09xg"
        }


        self.new_movie = {
            'title': 'new test',
            'release_date': '2015-20-11'
        }        
        
        self.new_actor = {
            'name': 'Abdelrahman',
            'age': 26,
            'gender': 'male'
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
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_all_actors(self):
        res = self.client().get('/actors', headers =self.producer_token)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) > 0)

   

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()