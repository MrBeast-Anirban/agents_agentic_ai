from crewai import Task
from pydantic import Field

class NewsTask(Task):
    api_key: str = Field(..., description="New York Times API key.")
    query: str = Field(..., description="Search query (default: 'sports').")
    page: int = Field(..., description="Number of articles to fetch.")

    def __init__(self, description, agent, api_key, query, page):
        super().__init__(
            description=description,  # Pass description as a keyword argument
            agent=agent  # Pass agent as a keyword argument
        )
        self.api_key = api_key
        self.query = query  # Default query is "sports"
        self.page = page  # 1 page and 10 articles

    def execute(self, task_outcome=None):
        """
        Execute the news task.
        
        :return: A list of news articles with titles, descriptions, and URLs.
        """
        return self.agent.get_latest_news(self.api_key, self.query, self.page)