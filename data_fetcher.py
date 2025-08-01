import requests
from typing import Dict, Optional


def get_current_weather(city: str, api_key: str, units: str = "metric") -> Optional[Dict]:
    """
    fetch current weather data for a given city from OpenWeatherMap API.

    args:
        city: City name (like "london")
        api_key: Openweathermap API key, i got mine off the website and u can use ur own if you pulled from my github
        units: metric or imperial

    returns:
        dictionary with weather data or none if the reuqest fails
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def get_forecast(city: str, api_key: str, units: str = "metric") -> Optional[Dict]:
    """
    fetches 5-day forecast data for a given city from OpenWeatherMap API.

    args:
        city: City name (like "london")
        api_key: Openweathermap API key, i got mine off the website and u can use ur own if you pulled from my github
        units: metric or imperial

    returns:
        dictionary with forecast data or none if request fails
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None