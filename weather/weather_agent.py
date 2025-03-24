import requests
from crewai import Agent

class WeatherAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Weather Reporter",
            goal="Fetch the current temperature and weather conditions of the user's location.",
            backstory="A knowledgeable agent that uses the OpenWeatherMap API to provide real-time weather information.",
            verbose=True
        )

    def get_weather(self, api_key, city_name):
        """
        Fetch the current temperature and weather conditions for a given city using the OpenWeatherMap API.
        
        :param api_key: Your OpenWeatherMap API key.
        :param city_name: The name of the city to fetch the weather for.
        :return: A dictionary containing the temperature and weather conditions.
        """
        try:
            # API endpoint and parameters
            url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city_name,
                "appid": api_key,
                "units": "metric"  # Use metric units for Celsius
            }

            # Make the API request
            response = requests.get(url, params=params)
            data = response.json()

            # Extract and return the temperature and weather conditions
            if response.status_code == 200:
                temperature = data["main"]["temp"]
                weather_conditions = data["weather"][0]["description"]
                return {
                    "temperature": temperature,
                    "conditions": weather_conditions,
                    "city": city_name
                }
            else:
                return {"error": data.get("message", "Unknown error")}
        except Exception as e:
            return {"error": f"Error fetching weather: {e}"}



    