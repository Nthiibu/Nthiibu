import requests

def get_weather(city: str, api_key: str):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve weather data. Check the city name or API key.")
        print(f"Error: {e}")
    except KeyError:
        print("Unexpected response format. Please check the city name and try again.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "your_api_key_here"  # Replace with your actual OpenWeatherMap API key
    get_weather(city, api_key)


