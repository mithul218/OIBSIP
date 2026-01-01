import requests

city_name = input("Enter city name: ")
api_key = '36eb6cb4572f55f202c93a0b6195c727'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&unit=metric'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Weather is ", data['weather'][0]['description'])
    print("Temperature is ", data['main']['temp'], "Celsius")
    print("Current Temperature feels like ", data['main']['feels_like'], "Celsius")
    print("Humidity is ", data['main']['humidity'], "%")