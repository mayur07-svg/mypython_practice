
import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your free OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    try:
        # Build complete URL
        complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"

        # Get response from server
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]

            weather = data["weather"][0]["description"]

            print(f"\nWeather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {weather.capitalize()}\n")

        else:
            print("City not found! Please enter a valid city name.")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    print("=== Simple Weather App ===")
    city_name = input("Enter city name: ")
    get_weather(city_name)

