"""
    2022 ALL RIGHTS RESERVED.
    Program created by Mori Keli.
    Created: 08/04/2022 0714hrs EAT

    Program fetches data from OpenWeather API.
"""
import requests

API_KEY = '##API key goes here>##'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

city = str(input('Enter a city name: '))

request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:     # HTTP Response Status
    data = response.json()
    weather = data['weather'][0]['description']     # fetch data from data via indexing - using dictionary
    temp = round(data['main']['temp']-273.15, 2)    # convert temp into Celsius and round to 2 decimal places.

    print(f'Weather: {weather}')
    print(f'Temperature: {temp} Celsius')
else:
    print("An error occurred.")
