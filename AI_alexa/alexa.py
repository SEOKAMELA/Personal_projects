from typing import Text
from pywhatkit.mainfunctions import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():

    try:
        with  sr.Microphone() as source:
            print("listening.... ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command: 
                command = command.replace("alexa",'')
                print(command)
    except:
        pass
    return command
        
def run_alexa():

    command = take_command()


    if "play" in command:
        song = command.replace('play', '')
        talk("playing .." + song)
        pywhatkit.playonyt(song)
    elif "search" in command:
        search = command.replace('search', '')
        pywhatkit.search(search)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('The time is '+time)
    
    elif 'what is' in command:
        question = command.replace('what is', '')
        info = wikipedia.summary(question,1)
        print(info)
        talk(info)
    elif 'who is' in command:
        question = command.replace('who is', '')
        info = wikipedia.summary(question,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I didnt unsersatnd that command please say it again')

while True:
    run_alexa()