import requests
from pprint import pprint
api_key = "f6ce8813b4cfca0fc8036e602d4b051b"
lat=41.3082
lon=-69.2598
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}exclude=current&appid={api_key}'

    # https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
r=requests.get(url)

pprint(r.json())