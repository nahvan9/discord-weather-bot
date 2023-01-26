
import requests

def getWeather(key, location):
    if location.startswith('<@'):
        import user_locations
        loc = user_locations.users[location.strip()]
    else:
        loc = location
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key={key}&q={loc}&aqi=no").json()

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