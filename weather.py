import requests

def get_weather(city_name, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        weather_report = data['weather']

        print(f"City: {city_name}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Weather Report: {weather_report[0]['description']}")
    else:
        print(f"Error getting the weather data. HTTP response code: {response.status_code}")

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = "your_openweathermap_api_key"  # Replace with your real OpenWeatherMap API Key
    get_weather(city_name, api_key)
