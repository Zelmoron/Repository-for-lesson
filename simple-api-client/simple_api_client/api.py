import requests

class SimpleAPIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        response = requests.get(f"{self.base_url}/{endpoint}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def post(self, endpoint, data):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data)
        if response.status_code == 201:
            return response.json()
        else:
            response.raise_for_status()
