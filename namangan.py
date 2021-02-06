import requests
from pprint import pprint
api_key = "f6ce8813b4cfca0fc8036e602d4b051b"
lat=40.9845254939922
lon=72.0620398798127
units = 'metric'
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units={units}&exclude=current&appid={api_key}'

    # https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
r=requests.get(url)
data=r.json()

pprint(data['timezone'])