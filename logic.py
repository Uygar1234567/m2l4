# Görev #3
from translate import Translator
import requests
from collections import defaultdict

# Görev #5

class TextAnalysis():   
    
    # Görev #1
    memory=defaultdict(list)
    def __init__(self, text, owner):

        # Görev #2
        TextAnalysis.memory[owner].append(self)
        self.text = text
        self.translation = self.__translate(self.text, "en", "ja")

        # Görev #6
        self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("YF-23 BLACK WIDOW", "en", "ja")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            # Görev #4
            translator= Translator(from_lang=from_lang, to_lang=to_lang)
            translation=translator.translate(text)
            return translation
        except:
            return "Çeviri girişimi başarısız oldu"


