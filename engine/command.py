import os
from tracemalloc import stop
from engine.config import *

import time
from zoneinfo import available_timezones
# This Module is ued to convert text to speech
import pyttsx3

# This module is used to recoginize speech command
import speech_recognition as sr


# This Module is used to play sounds and music
from playsound import playsound

import eel

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 174)


def speak(audio):
    engine.say(audio)
    eel.SpeakMessage(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        eel.SpeakMessage("Listening...")
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    try:
        print("Recoginizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
        eel.SpeakMessage(query)
        time.sleep(2)
        # eel.sleep(1.0)
    except Exception as e:
        return "none"
    return query.lower()


@eel.expose
def allCommands(typequery=1):
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    histring = 'hi '+ASSISTANT_NAME
    print()
    # input from chatbox
    if typequery == 1:
        query = takecommand()
    else:
        eel.SpeakMessage(typequery)
        time.sleep(2)
        query = typequery

    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "close" in query:
        from engine.features import close
        close(query)

    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)

    elif "weather" in query:
        from engine.features import weather
        weather(query)

    elif "call disconnect" in query or "disconnect call" in query or "stop call" in query:
        from engine.features import DisconnectCall
        DisconnectCall()

    elif query == "call":
        speak("who do you want to call ?")
        query = takecommand()
        from engine.features import MakeCall
        MakeCall(query)

    elif "call" in query or "phone" in query:
        from engine.features import MakeCall
        MakeCall(query)

    elif "happy" in query or "day" in query:
        speak("Thank You Sir")

    elif "battery status" in query or "power status" in query:
        from engine.features import battery
        battery()

    elif "shutdown" in query or "power off" in query:
        speak("shutdown process started")
        speak("Have a good day "+OWNER_NAME)
        os.system('shutdown -s')

    else:
        if query == "none":
            print(query)
            pass
        else:
            from engine.bot import bot
            returnString = bot(query)
            if returnString != 0:
                speak(returnString)
            else:
                from engine.features import chatGPT
                print("chat gpt run")
                chatGPT(query)
    eel.hideSpectrum()
