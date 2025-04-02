from crewai import Agent
from text_similarity import TextSimilarity
from web_search import WebSearch

class PlagiarismDetectionAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Plagiarism Detector",
            goal="Detect plagiarism in a given text by comparing it to online sources.",
            backstory="A vigilant agent trained to identify copied or unoriginal content by searching the internet.",
            verbose=True
        )

    def detect_plagiarism(self, text, threshold=0.5, num_results=5, api_key="####Removed this as of now######"):
        """
        Detect plagiarism in a given text by searching the internet for similar content.
        
        :param text: The text to check for plagiarism.
        :param threshold: The similarity threshold to consider as plagiarism (default: 0.8).
        :param num_results: Number of search results to fetch (default: 5).
        :param api_key: API key for SerpAPI (optional).
        :return: A list of tuples containing the reference text and its similarity score.
        """
        # Initialize utilities
        text_similarity = TextSimilarity()
        web_search = WebSearch(api_key=api_key)

        # Extract keywords or use a more concise query
        query = " ".join(text.split()[:10])  # Use the first 10 words as the search query

        # Search the internet for similar content
        reference_texts = web_search.search_google(query, num_results=num_results)

        # Compare the text with search results
        results = []
        for ref_text in reference_texts:
            similarity = text_similarity.calculate_similarity(text, ref_text)
            if similarity >= threshold:
                results.append((ref_text, similarity))
        return results
