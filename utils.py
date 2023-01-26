
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
    
    # Add condition emotes
    conditionEmote = ''
    if 'rain' in condition.lower():
        conditionEmote = ':cloud_rain:'
    elif 'sun' in condition.lower():
        conditionEmote = ':sunny:'
    elif 'cloudy' in condition.lower():
        conditionEmote = ':cloud:'
    elif 'snow' in condition.lower():
        conditionEmote = ':cloud_snow:'
    else:
        conditionEmote = ':exclamation:'
        
    wind = response['current']['wind_mph']
    windGust = response['current']['gust_mph']
    windDir = response['current']['wind_dir']
    humidity = response['current']['humidity']
    cloudCoverage = response['current']['cloud']

    msg = f'{conditionEmote} {condition}. :thermometer: Temperature: {tempC} C/{tempF} F\
    \n:dash: Wind: {windDir} at {wind} mph gusting to {windGust} mph.\
    \n:droplet: Humidity: {humidity}%, Cloud Coverage: {cloudCoverage}%. \n '

    return msg