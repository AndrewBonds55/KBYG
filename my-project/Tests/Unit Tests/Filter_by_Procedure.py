def test_filter_by_procedure_type(self):
    with self.app.test_client() as client:
        response = client.get('/dental_offices?zip_code=12345&procedure_type=cleaning')
        data = response.get_json()
        assert len(data) > 0
        for office in data:
            assert 'cleaning' in office['prices']
