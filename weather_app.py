import requests

def get_weather(api_key, location):
    # OpenWeatherMap API endpoint for current weather
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    
    # Specify the parameters (you can use either zip code or city name)
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric',  # You can change units to 'imperial' for Fahrenheit
    }

    # Make the API request
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: {response.status_code}")
        return None

def main():
    # Replace 'YOUR_API_KEY' with the API key you obtained from OpenWeatherMap
    api_key = '2606f769271b8d545fe3458b2b72ed9f'

    location = input("Enter zip code or city name: ")
    
    weather_data = get_weather(api_key, location)

    if weather_data:
        # Extract and print relevant weather information
        print(f"Weather in {location}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()
