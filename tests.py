import requests


class TestTaxiData:
    headers = {'Authorization': 'Token e1c7b8d5a0d5fc0c22e5c44302e7ec9b36354a23'}
    base_url = 'http://127.0.0.1:8000/api/v1/taxi_data/'

    def test_get_data(self):
        data = requests.get(url=self.base_url, headers=self.headers)

        assert data.status_code == 200

    def test_get_unique_data(self):
        data = requests.get(url=f'{self.base_url}177/', headers=self.headers)

        assert data.status_code == 200


