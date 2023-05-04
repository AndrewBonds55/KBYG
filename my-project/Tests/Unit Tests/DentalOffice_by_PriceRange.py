def test_filter_by_price_range(self):
    with self.app.test_client() as client:
        response = client.get('/dental_offices?zip_code=12345&min_price=50&max_price=100')
        data = response.get_json()
        assert len(data) > 0
        for office in data:
            for price in office['prices'].values():
                assert 50 <= price <= 100