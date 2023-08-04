from googletrans import Translator

def translate(text, lang):
    translator = Translator()
    result = translator.translate(text, dest=lang)

    return result.text