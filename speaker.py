import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=320
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print("User said :" ,query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query