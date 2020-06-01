from main import get_temperature
import pytest
import requests
def test_get_temperature_by_lat_lng():
    lat = -14.235004
    lng = -51.92528
    temperature_c = get_temperature(lat,lng)
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    reponse = requests.get(url)
    data = reponse.json()
    temperature_f = data.get('currently').get('temperature')
    temperature_coverted = int((5/9)*(temperature_f-32))
    assert temperature_c == temperature_coverted