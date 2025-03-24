from crewai import Task
from pydantic import Field

class WeatherTask(Task):
    api_key: str = Field(..., description="OpenWeatherMap API key.")
    city_name: str = Field(..., description="Name of the city to fetch the weather for.")

    def __init__(self, description, agent, api_key, city_name):
        super().__init__(
            description=description,  # Pass description as a keyword argument
            agent=agent  # Pass agent as a keyword argument
        )
        self.api_key = api_key
        self.city_name = city_name

    def execute(self, task_outcome=None):
        """
        Execute the weather task.
        
        :return: A formatted string with the temperature and weather conditions.
        """
        weather_data = self.agent.get_weather(self.api_key, self.city_name)
        if "error" in weather_data:
            return weather_data["error"]
        else:
            return (
                f"The current temperature in {weather_data['city']} is {weather_data['temperature']}°C. "
                f"The weather conditions are {weather_data['conditions']}."
            )

