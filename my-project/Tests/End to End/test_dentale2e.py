import unittest
from app import create_app, db
from app.models import Procedure

class TestDentalPriceDatabase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        # Add some procedures to the database for testing
        root_canal = Procedure(name='Root Canal', cost=1000)
        teeth_whitening = Procedure(name='Teeth Whitening', cost=500)
        db.session.add_all([root_canal, teeth_whitening])
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_search_procedure_cost(self):
        # Test that a user can search for a procedure and see the correct cost
        response = self.client.get('/search?procedure=Root Canal')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'$1,000', response.data)
        
    def test_add_procedure(self):
        # Test that a user can add a new procedure to the database
        response = self.client.post('/add', data=dict(name='Filling', cost=200))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Procedure.query.filter_by(name='Filling').count(), 1)
        
    def test_update_procedure_cost(self):
        # Test that a user can update the cost of a procedure in the database
        response = self.client.post('/update', data=dict(name='Teeth Whitening', cost=600))
        self.assertEqual(response.status_code, 302)
        teeth_whitening = Procedure.query.filter_by(name='Teeth Whitening').first()
        self.assertEqual(teeth_whitening.cost, 600)
        
if __name__ == '__main__':
    unittest.main()


#In this example, we are creating a Flask application in testing mode and setting up a test client to simulate user interactions with the application. We then add some procedures to the database for testing. 

#The `test_search_procedure_cost` method tests that a user can search for a procedure and see the correct cost. The `test_add_procedure` method tests that a user can add a new procedure to the database. The `test_update_procedure_cost` method tests that a user can update the cost of a procedure in the database.


#We then run the tests using the `unittest` module. These tests ensure that the dental price database is working correctly and that users can search for, add, and update procedures in the database through the Flask application.
