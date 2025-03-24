from crewai import Crew
from plagiarism_detection_agent import PlagiarismDetectionAgent
from plagiarism_detection_task import PlagiarismDetectionTask

def main():
    # Create the plagiarism detection agent
    plagiarism_agent = PlagiarismDetectionAgent()

    # Define the text to check for plagiarism
    text = "Artificial intelligence is transforming the world by enabling machines to learn from data."

    # Create a plagiarism detection task
    plagiarism_task = PlagiarismDetectionTask(
        description="Detect plagiarism in the given text by searching the internet.",
        agent=plagiarism_agent,
        text=text,
        threshold=0.5,  # Lower the threshold
        num_results=5,  # Number of search results to fetch
        api_key="5ab6c2ed2ef9f7725279723070a0667e867afe9aa879a2233bc327d373cda1e8"  # Optional: Add your SerpAPI key
    )

    # Create a crew and add the task
    crew = Crew(
        agents=[plagiarism_agent],
        tasks=[plagiarism_task],
        verbose=True
    )

    # Execute the crew
    result = crew.kickoff()
    print(f"Text to Check: {text}")
    print("Plagiarism Detection Results:")
    for ref_text, similarity in result:
        print(f"- Reference Text: {ref_text}")
        print(f"  Similarity: {similarity:.2f}")

if __name__ == "__main__":
    main()