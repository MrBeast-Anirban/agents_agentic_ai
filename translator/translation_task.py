from crewai import Task
from pydantic import Field

class TranslationTask(Task):
    text: str = Field(..., description="The text to translate.")
    src_lang: str = Field(default='auto', description="Source language code.")
    dest_lang: str = Field(default='en', description="Destination language code.")

    def __init__(self, description, agent, text, src_lang='auto', dest_lang='en'):
        super().__init__(
            description=description,  # Pass description as a keyword argument
            agent=agent  # Pass agent as a keyword argument
        )
        self.text = text
        self.src_lang = src_lang
        self.dest_lang = dest_lang

    def execute(self, task_outcome=None):
        """
        Execute the translation task.
        
        :param task_outcome: Optional argument passed by the Crew class (unused in this task).
        :return: Translated text.
        """
        return self.agent.translate(self.text, self.src_lang, self.dest_lang)