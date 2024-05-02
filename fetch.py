from urllib.request import urlopen
import certifi
import json
from os.path import dirname, join

api = {}
api["url"] = "https://financialmodelingprep.com/api/v3/"

current_dir = dirname(__file__)
file_path = join(current_dir, "./api-key.json")
with open(file_path, 'r') as f:
    api["key"] = json.load(f)["key"]


def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

class Stock:
    def __init__(self, tag) -> None:
        self.tag = tag
        self.get_profile()

    def get_profile(self):
        url = api["url"] + f'profile/{self.tag}?apikey={api["key"]}'


apple = Stock("AAPL")
