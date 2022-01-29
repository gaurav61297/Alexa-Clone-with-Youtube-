import speech_recognition as sr
import pyttsx3
import pywhatkit


def talk(command):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say("I am alexa what can i do for you")
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening...talk aloud dear")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            song=command.replace('play','')
            talk(song)
            pywhatkit.playonyt(song)

    except:
        pass

take_command()