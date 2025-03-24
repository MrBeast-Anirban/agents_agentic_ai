from googletrans import Translator

class TranslatorUtil:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, src_lang='auto', dest_lang='en'):
        """
        Translate text from one language to another.
        
        :param text: The text to translate.
        :param src_lang: Source language code (e.g., 'en' for English, 'auto' for auto-detection).
        :param dest_lang: Destination language code (e.g., 'hi' for Hindi, 'fr' for French).
        :return: Translated text.
        """
        try:
            translation = self.translator.translate(text, src=src_lang, dest=dest_lang)
            return translation.text
        except Exception as e:
            return f"Translation failed: {e}"