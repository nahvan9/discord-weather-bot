
import requests

from geopy.geocoders import Nominatim


# def getCoords(addr):
#     geolocator = Nominatim(user_agent="App")
#     location = geolocator.geocode(addr)

#     return location.latitude, location.longitude


def getWeather(key, location):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no").json()

    tempC = response['current']['temp_c']
    tempF = response['current']['temp_f']
    condition = response['current']['condition']['text']
    wind = response['current']['wind_mph']
    windGust = response['current']['gust_mph']
    windDir = response['current']['wind_dir']
    humidity = response['current']['humidity']
    cloudCoverage = response['current']['cloud']


    msg = f'{condition}. Temps around {tempC} C/{tempF} F\
    \nWind {windDir} at {wind} mph gusting to {windGust} mph.\
    \nHumidity {humidity}%, and cloud coverage at {cloudCoverage}%. '

    return msg