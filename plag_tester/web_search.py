import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch

class WebSearch:
    def __init__(self, api_key=None):
        self.api_key = api_key  # API key for SerpAPI (optional)

    def search_google(self, query, num_results=5):
        """
        Search Google for the given query and return the top results.
        
        :param query: The search query.
        :param num_results: Number of results to return.
        :return: List of search results (text snippets).
        """
        if self.api_key:
            # Use SerpAPI for more reliable and structured results
            params = {
                "q": query,
                "api_key": self.api_key,
                "num": num_results
            }
            search = GoogleSearch(params)
            results = search.get_dict().get("organic_results", [])
            return [result.get("snippet", "") for result in results]
        else:
            # Fallback to simple web scraping (less reliable)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            url = f"https://www.google.com/search?q={query}"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            results = []
            for g in soup.find_all("div", class_="tF2Cxc"):
                snippet = g.find("div", class_="IsZvec")
                if snippet:
                    results.append(snippet.text)
                if len(results) >= num_results:
                    break
            return results