from crewai import Task
from pydantic import Field

class PlagiarismDetectionTask(Task):
    text: str = Field(..., description="The text to check for plagiarism.")
    threshold: float = Field(default=0.8, description="The similarity threshold to consider as plagiarism.")
    num_results: int = Field(default=5, description="Number of search results to fetch.")
    api_key: str = Field(default=None, description="API key for SerpAPI (optional).")

    def __init__(self, description, agent, text, threshold=0.8, num_results=5, api_key=None):
        super().__init__(
            description=description,  # Pass description as a keyword argument
            agent=agent  # Pass agent as a keyword argument
        )
        self.text = text
        self.threshold = threshold
        self.num_results = num_results
        self.api_key = api_key

    def execute(self, task_outcome=None):
        """
        Execute the plagiarism detection task.
        
        :return: A list of tuples containing the reference text and its similarity score.
        """
        return self.agent.detect_plagiarism(self.text, self.threshold, self.num_results, self.api_key)