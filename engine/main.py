import os
import time
# from engine.config import *

import time
from zoneinfo import available_timezones
# This Module is ued to convert text to speech
import pyttsx3

# This module is used to recoginize speech command
import speech_recognition as sr

from click import command

MoNo = '7620464305'
# command = 'adb shell am start -a android.intent.action.CALL -d tel:+91'+MoNo
command1 = 'adb shell service call phone 5'  # ------ to reject call
# command2 = 'adb shell input keyevent 5' -------------- to receive call

# print('calling...')
os.system(command1)


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices[0].id)
# engine.setProperty('voice', voices[1].id)
# print(voices)
# engine.setProperty('rate', 174)


# def speak(audio):

#     engine.say(audio)
#     engine.runAndWait()


# speak("Hello, I am Digambar")
