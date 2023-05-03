import unittest
from app import create_app, db
from app.models import Procedure

class TestDentalPriceDatabase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
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
        
    def test_procedure_cost(self):
        # Test that the cost of a procedure is correctly returned
        root_canal = Procedure.query.filter_by(name='Root Canal').first()
        self.assertEqual(root_canal.cost, 1000)
        
    def test_add_procedure(self):
        # Test that a new procedure can be added to the database
        filling = Procedure(name='Filling', cost=200)
        db.session.add(filling)
        db.session.commit()
        self.assertEqual(Procedure.query.filter_by(name='Filling').count(), 1)
        
    def test_update_procedure_cost(self):
        # Test that the cost of a procedure can be updated
        teeth_whitening = Procedure.query.filter_by(name='Teeth Whitening').first()
        teeth_whitening.cost = 600
        db.session.commit()
        self.assertEqual(teeth_whitening.cost, 600)
        
if __name__ == '__main__':
    unittest.main()
