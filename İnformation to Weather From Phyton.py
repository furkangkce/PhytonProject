import requests
## make a program for give information for weather
def weather():
    city = input("Enter city for the weather: ")
    api_key = "Enter Api Key"
    url = "http://api.openweathermap.org/data/2.5/weather"


    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        info = response.json()
        temperature = info["main"]["temp"]
        wind_speed = info["wind"]["speed"]
        weather_desc = info["weather"][0]["description"]

        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature} °C")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Weather: {weather_desc}")
    else:
        print("City not found or API error!")


weather()
