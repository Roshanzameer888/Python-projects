import requests

def get_weather(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key}

    response = requests.get(base_url, params=params)
    weather_data = response.json()

    # Extract and display relevant weather information
    if weather_data['cod'] == '404':
        print("City not found.")
    else:
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"Temperature: {temperature}K, Description: {description}")

# Example usage
api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
city = 'London'
get_weather(api_key, city)
