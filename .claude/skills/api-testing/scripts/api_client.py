import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get(self, endpoint, **kwargs):
        return self.session.get(f"{self.base_url}/{endpoint}", **kwargs)
    
    def post(self, endpoint, **kwargs):
        return self.session.post(f"{self.base_url}/{endpoint}", **kwargs)
