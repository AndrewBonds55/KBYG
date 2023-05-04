def test_database_returns_data(self):
    with self.app.test_client() as client:
        response = client.get('/dental_offices?zip_code=12345')
        data = response.get_json()
        assert len(data) > 0