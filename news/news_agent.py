import requests
from crewai import Agent

class NewsAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Filterd News Fetcher",
            goal="Fetch the latest query based news articles from The New York Times.",
            backstory="A knowledgeable agent that uses The New York Times API to provide domain filtered real-time news updates.",
            verbose=True
        )

    def get_latest_news(self, api_key, query, page):
        """
        Fetch the latest news articles using The New York Times API.
        
        :param api_key: Your New York Times API key.
        :param query: Search query (default: "sports").
        :param num_articles: Number of articles to fetch (default: 5).
        :return: A list of news articles with titles, descriptions, and URLs.
        """
        try:
            # API endpoint and parameters
            url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q={}&api-key={}".format(query, api_key)
            params = {
                "sort": "newest",  # Sort by newest articles
            }
            # Make the API request
            response = requests.get(url)
            data = response.json()

            # Extract and return the news articles
            if response.status_code == 200:
                articles = data["response"]["docs"]
                return [
                    {
                        "title": article["headline"]["main"],
                        "description": article["abstract"],
                        "url": article["web_url"]
                    }
                    for article in articles
                ]
            else:
                return [{"error": data.get("fault", {}).get("faultstring", "Unknown error")}]
        except Exception as e:
            return [{"error": f"Error fetching news: {e}"}]