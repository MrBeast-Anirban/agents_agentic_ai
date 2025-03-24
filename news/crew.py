from crewai import Crew
from news_agent import NewsAgent
from news_task import NewsTask

def main():
    # Create the news agent
    news_agent = NewsAgent()

    # Define the API key, query, and number of articles
    api_key = "EgzM74IS0ptUg9b5jGqBgF4kSrcfIwUS"  # Replace with your New York Times API key
    query = "education"  # Query for education news
    page = 1  # Page number for pagination

    # Create a news task
    news_task = NewsTask(
        description="Fetch the latest {} news articles from The New York Times.".format(query),
        agent=news_agent,
        api_key=api_key,
        query=query,  # Pass the query dynamically
        page=page  # Pass the page number dynamically
    )

    # Create a crew and add the task
    crew = Crew(
        agents=[news_agent],
        tasks=[news_task],
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()
    print("Latest {} News from The New York Times:".format(query))

    # File path for saving the output
    file_path = "output.txt"

    # Open the file in write mode
    with open(file_path, 'w') as file:
        for article in result:
            if "error" in article:
                file.write(f"Error: {article['error']}\n\n")
            else:
                print(f"- Title: {article['title']}")
                print(f"  Description: {article['description']}")
                print(f"  URL: {article['url']}")
                print()

                # Write article details to the file
                file.write(f"- Title: {article['title']}\n")
                file.write(f"  Description: {article['description']}\n")
                file.write(f"  URL: {article['url']}\n\n")

    print(f"File '{file_path}' created successfully.")

if __name__ == "__main__":
    main()