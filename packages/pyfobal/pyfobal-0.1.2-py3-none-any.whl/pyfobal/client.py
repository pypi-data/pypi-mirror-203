import requests
 
class Client:
    def __init__(self, api_key, api_version='v1'):
        self.base_url = f"https://api.example.com/{api_version}"
        self.api_key = api_key
        self.headers = {'Authorization': f'Bearer {self.api_key}'}

    def _make_request(self, endpoint):
        url = f'{self.base_url}{endpoint}'
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def _process_data(self, data, entity_class):
        return [entity_class(item) for item in data]

 
    def get_leagues(self):
            return "Hello from get_leagues()"