import unittest
from flask import Flask, request
from app import search

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_search(self):
        with self.app.test_request_context('/search', method='POST', data={'location': '12345'}):
            response = search()
            assert response.status_code == 200
            assert b'Results' in response.data

if __name__ == '__main__':
    unittest.main()
