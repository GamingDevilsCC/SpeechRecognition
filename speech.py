import speech_recognition as sr
from googletrans import Translator

r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        print("Say anything!")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if text == "quit":
                print("Goodbye!")
                break
            trans = Translator()
            t = trans.translate(text, src = 'en', dest = 'fr')
            print("You said:", text)
            print("In french:", t.text)

        except:
            print("I was not able to convert your speech.\nPlease try again.")
