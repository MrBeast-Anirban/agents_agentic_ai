from crewai import Crew
from translation_agent import TranslationAgent
from translation_task import TranslationTask

def main():
    # Create the translation agent
    translation_agent = TranslationAgent()

    # Define the text to translate
    text = "Hello, My name is Anirban Maitra"
    src_lang = 'en'  # Source language (English)
    dest_lang = 'hi'  # Destination language (Hindi)

    # Create a translation task
    translation_task = TranslationTask(
        description=f"Translate text from {src_lang} to {dest_lang}",
        agent=translation_agent,
        text=text,
        src_lang=src_lang,
        dest_lang=dest_lang
    )

    # Create a crew and add the task
    crew = Crew(
        agents=[translation_agent],
        tasks=[translation_task],
        verbose=True  # Ensure this is a boolean value
    )

    # Execute the crew
    result = crew.kickoff()
    #print(f"Original Text ({src_lang}): {text}")
    #print(f"Translated Text ({dest_lang}): {result}")

if __name__ == "__main__":
    main()