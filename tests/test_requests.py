import requests

def test_200_status_code():
    url = 'https://vice-city-api-kostyafarber.koyeb.app/stations/K-Chat'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_404_status_code():
    url = 'https://vice-city-api-kostyafarber.koyeb.app/stations/DoesNotExist'
    resp = requests.get(url)
    assert resp.status_code == 404