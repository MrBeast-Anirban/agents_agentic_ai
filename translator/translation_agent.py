from crewai import Agent
from translator import TranslatorUtil

class TranslationAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Translator",
            goal="Translate text from one language to another",
            backstory="A multilingual agent specialized in translation tasks.",
            verbose=True  # Enable verbose logging
        )

    def translate(self, text, src_lang='auto', dest_lang='en'):
        """
        Translate text from one language to another.
        
        :param text: The text to translate.
        :param src_lang: Source language code.
        :param dest_lang: Destination language code.
        :return: Translated text.
        """
        translator_util = TranslatorUtil()  # Create a TranslatorUtil instance
        return translator_util.translate_text(text, src_lang, dest_lang)