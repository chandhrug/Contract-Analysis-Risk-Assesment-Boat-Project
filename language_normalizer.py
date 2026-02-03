

from googletrans import Translator

translator = Translator()

def normalize_hindi_to_english(text):
    if not text:
        return ""
    try:
        return translator.translate(text, src="hi", dest="en").text
    except:
        return text
