from engine.config import *
from unittest import result
import requests
from bs4 import BeautifulSoup
import json
from ast import dump
from audioop import avgpp
from sys import path
import sys
import eel
from pyparsing import Empty

# This Module is ued to convert text to speech
import pyttsx3

# This module is used to recoginize speech command
import speech_recognition as sr

# Date Time Module to get current date and time
import datetime

# Wkipedia Module to search things on wikipedia
import wikipedia

# OS Module To work On Windows Like Open notepad or cmd
import os

# This Module is use to get time
import time

# This Module is used to play sounds and music
from playsound import playsound

# This module is used to open web browser
import webbrowser

# Give Randoms Facts
# import randfacts

# This function is used to send message or search on google
import pywhatkit as kit

# this module is used to automate system or uses keyboaed keys and mouse
import pyautogui as autogui


# python script showing battery details
import psutil

import sqlite3


# Global Declaration
connection = sqlite3.connect('assistant.sqlite')
cursor = connection.cursor()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 174)

# text to speech


def speak(audio):
    engine.say(audio)
    eel.WishMessage(audio)
    eel.SpeakMessage(audio)
    engine.runAndWait()
    return audio
# Battery status function


def battery():
    # function returning time in hh:mm:ss
    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)

    battery = psutil.sensors_battery()
    speak("Sir, Your Battery Status is: ")
    print("Battery percentage : ", battery.percent)
    speak(f"Battery Percentage: {battery.percent}")

    if battery.power_plugged == True:

        print("Power plugged in : ON")
        speak("Power plugged in is on")

    else:
        print("Power plugged in : OFF")
        speak("Power plugged in is OFF")

    batteryRemaning = str(convertTime(battery.secsleft))
    batterylist = batteryRemaning.split(':')

    speak(
        f"Battery left: {batterylist[0]} hours, {batterylist[1]} minutes, {batterylist[2]} seconds")
    print("Battery left : ", convertTime(battery.secsleft))

# Loading Effect


def loading():
    music_dir = "audio\\alert sound\\bell_alert.wav"
    speak("System Initiating")
    playsound(music_dir)
    speak("Initializing Database")
    eel.TextSet("Initializing Database")
    playsound(music_dir)
    speak("Adding All The Preferances")
    eel.TextSet("Adding All The Preferances")
    playsound(music_dir)
    speak("System is now fully operational")
    eel.TextSet("Starting ...")


# Time Whiches function
def wish():

    hour = int(datetime.datetime.now().hour)
    currentTime = datetime.datetime.now()
    currentTime = currentTime.strftime(
        '%I %M %p').lstrip("0").replace(" 0", " ")
    if hour > 0 and hour < 12:
        speak("Hello, Good Morning Boss")
        speak(" it's "+currentTime)
        speak("I am "+ASSISTANT_NAME+", Your Personal assistant")

    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon Boss")
        speak("it's"+currentTime)
        speak(" I am Sofia, Your Personal assistant")
    else:
        eel.WishMessage(speak("Hello, Good Evening Boss"))
        eel.WishMessage(speak("it's " + currentTime))
        eel.WishMessage(speak("I am "+ASSISTANT_NAME))
        eel.WishMessage(speak("How can i help you"))

# Open Commands


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    # System Command
    if query in query:
        cursor.execute(
            "SELECT path FROM sys_command WHERE name='%s'" % query.strip())
        results = cursor.fetchall()
        if len(results) != 0:
            flag = results[0]
            path = flag[0]
            repr(path)
            speak("Opening "+query)
            os.startfile(path)
        else:
            cursor.execute(
                "SELECT path FROM web_command WHERE name='%s'" % query.strip())
            results = cursor.fetchall()
            if len(results) != 0:
                flag = results[0]
                path = flag[0]
                repr(path)
                speak("Opening "+query)
                webbrowser.open(path)
            else:
                speak(query+" Not Found !")
    else:
        pass


# openCommand(" notepad")


def close(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("close", "")

    if "notepad" in query:
        speak("Closing Notepad")
        os.system("TASKKILL /F /IM notepad.exe")

    elif "chrome" in query:
        speak("closing chrome")
        os.system("TASKKILL /F /IM chrome.exe")

    elif "xampp" in query:
        speak("closing xampp")
        os.system("TASKKILL /F /IM xampp-control.exe")

    elif "spotify" in query:
        speak("closing spotify")
        os.system("TASKKILL /F /IM spotify.exe")

    else:
        pass

# search on web browser


def searchTerm(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("search", "")
    speak("please sir, wait for a minute")

    kit.search(query)
    speak("here what i found on web")
    # term = wikipedia.summary(query, sentences=2)
    # speak(term)

# Play On YouTube


def PlayYoutube(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("search", "")
    query = query.replace("play", "")
    query = query.replace("on youtube", "")
    speak("Playing"+query+"on YouTube")
    kit.playonyt(query)

# Random Facts


# def RandomFacts():
#     fact = randfacts.getFact()
#     speak(fact)
#     print(fact)


# minimize all open window
def MinimizeOpenWindows():
    autogui.keyDown("win")
    autogui.press("d")
    time.sleep(2)
    autogui.keyUp("win")

# maximize all open window


def MaximizeOpenWindows():
    autogui.keyDown("win")
    autogui.press("d")
    time.sleep(2)
    autogui.keyUp("win")


def copy():
    autogui.hotkey('ctrl', 'c')


def paste():
    autogui.hotkey('ctrl', 'v')


#  ************************************************** WEATHER METHOD **********************************************

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather+"°C")
    eel.weatherShow(info, weather+" °C", location, time)
    speak("its "+weather+" degree celsius and "+info+" in "+location)

#  ************************************************** WEATHER METHOD **********************************************


# def bot():
#     f = open('bot.json')
#     jtopy = json.dumps(f)
#     data = json.loads(jtopy)

# Iterating through the json
# list
# for i in data['data']:
#     print(i)

# Closing file
# f.close()


# bot()


# Make Phone Call Command
def MakeCall(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("call", "")
    query = query.replace("make a", "")
    query = query.replace("phone", "")
    query = query.replace("call", "")
    print(query.strip())
    cursor.execute(
        "SELECT mobileno FROM phonebook WHERE name='%s'" % query.strip().lower())
    results = cursor.fetchall()
    if len(results) != 0:
        speak("Calling "+query)
        flag = results[0]
        MobileNo = flag[0]
        command = 'adb shell am start -a android.intent.action.CALL -d tel:+91'+MobileNo
        os.system(command)
    else:
        speak('No Data Found')
