import unittest
from app import create_app, db
from app.models import DentalOffice

class TestDentalOfficeDatabase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
        
    def test_add_dental_office(self):
        # Test that a new dental office can be added to the database
        dental_office = DentalOffice(name='Healthy Smiles', address='123 Main St', city='Anytown', state='CA', zip_code='12345')
        db.session.add(dental_office)
        db.session.commit()
        self.assertEqual(DentalOffice.query.filter_by(name='Healthy Smiles').count(), 1)
        
if __name__ == '__main__':
    unittest.main()

 #  In this example, we are creating a Flask application in testing mode and setting up a test database.

#The `test_add_dental_office` method tests that a new dental office can be added to the database. We create a new `DentalOffice` object and add it to the database using SQLAlchemy. We then check that the database contains the new dental office.

#We then run the test using the `unittest` module. This test ensures that a new dental office can be added to the database and that the database is correctly integrated with the Flask application. 