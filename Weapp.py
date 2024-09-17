import requests

api = open('api_key.txt', 'r').read()

location = input("Select your location: ")

result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api}')

print(result.json())

description = result.json()['weather'][0]['description']
print(description)