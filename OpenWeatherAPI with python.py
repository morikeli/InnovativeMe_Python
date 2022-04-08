"""
    2022 ALL RIGHT RESERVED.
    Program developed, debugged & maintained by Mori Keli.
    Created 08/04/2022 12:43pm EAT

    What's New?
    ------------------
    * Functional Programming
    * New Parameters(wind speed, humidity, pressure & country code)
    * Log file included
"""
# Python program that integrates OpenWeatherAPI and display weather condition of a given city.

import requests
import datetime
current_date = datetime.datetime.today().strftime('%a %dth-%m-%Y %H:%M:%S')

API_KEY = '2f39d8d235dae6ac6175dd151d49b198'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


def city_name(city):
    request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
    response = requests.get(request_url)
    if not response.status_code == 200:
        return 'An error occurred.'

    if response.status_code == 200:  # HTTP Response Status
        data = response.json()
        # print(data)
        weather = data['weather'][0]['description']  # fetch data from data via indexing - using dictionary
        temp = round(data['main']['temp'] - 273.15, 2)  # convert temp into Celsius and round to 2 decimal places.
        country = data['sys']['country']
        wind_speed = data['wind']['speed']
        humidity = data['main']['pressure']
        pressure = data['main']['humidity']

        program_data = {
            'City': f'{city}, {country}',
            'Weather': str(weather).title(),
            'Temperature': temp,
            'Humidity': humidity,
            'Wind speed': wind_speed,
            'Pressure': pressure,

        }
        with open('data.txt', 'a') as logfile:
            print('---'*30)
            print(f'Date fetched: {current_date}', file=logfile)
            print(program_data, file=logfile)
            logfile.close()

        return f'City: {city}, {country} \nWeather: {str(weather).title()} \nTemperature: {temp} Celsius.\nHumidity: {humidity}\nWind Speed: ' \
               f'{wind_speed} m/s\nPressure: {pressure}'


print(city_name(city=str(input('Enter city name: ')).title()))

