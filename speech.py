import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say anything!")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("Output:", text)
    except:
        print("I was not able to convert your speech.\nPlease try again.")
        