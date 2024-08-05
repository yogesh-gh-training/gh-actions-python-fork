import os
import requests

def test_geocoding_api():
    url = f"{os.environ['API_URL_GEOCODING']}/search?name=Bangalore"
    response = requests.get(url)
    assert response.status_code == 200, "Geocoding API failed"

def test_weather_api():
    url = f"{os.environ['API_URL_WEATHER']}/forecast?latitude=12.97&longitude=77.59&hourly=temperature_2m"
    response = requests.get(url)
    assert response.status_code == 500, "Weather API failed"

if __name__ == "__main__":
    test_geocoding_api()
    test_weather_api()
    print("All tests passed")
