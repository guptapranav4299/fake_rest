# 1. FACTORY PATTERN

class French:
    def __init__(self):
        self.translations = {"book": "voiture", "phone": "biclothtte",
                             "cloth": "clothtte"}

    def localize(self,message):
        return self.translations.get(message)

class Spanish:
    def __init__(self):
        self.translations = {"book": "libro", "phone": "teléfono",
                             "cloth": "paño"}

    def localize(self,message):
        return self.translations.get(message)


class English:

    def localize(self,message):
        return message

def factory(language= "English"):
    localizers = {
        "French":French,
        "Spanish":Spanish,
        "English":English
    }

    return localizers[language]()

if __name__ == "__main__":
    fr = factory("French")
    sp = factory("Spanish")
    en = factory("English")

    message = ["book","phone","cloth"]

    for m in message:
        print(fr.localize(m))
        print(sp.localize(m))
        print(en.localize(m))

