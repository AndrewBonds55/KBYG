def test_database_returns_correct_price(self):
    with self.app.test_client() as client:
        response = client.get('/dental_offices?zip_code=12345')
        data = response.get_json()
        for office in data:
            if office['name'] == 'Example Dental Office':
                assert office['prices']['cleaning'] == 100