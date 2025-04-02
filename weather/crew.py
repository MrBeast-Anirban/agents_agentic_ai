from crewai import Crew
from weather_agent import WeatherAgent
from weather_task import WeatherTask

def main():
    # Create the weather agent
    weather_agent = WeatherAgent()

    # Define the API key and city name
    api_key = "####Removed this as of now####"  # Replace with your OpenWeatherMap API key
    city_name = "Jodhpur"  # Replace with your city name

    # Create a weather task
    weather_task = WeatherTask(
        description="Fetch the current temperature and weather conditions of the user's location.",
        agent=weather_agent,
        api_key=api_key,
        city_name=city_name
    )

    # Create a crew and add the task
    crew = Crew(
        agents=[weather_agent],
        tasks=[weather_task],
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    main()


