# This Module is ued to convert text to speech
import threading
import pyttsx3


engine = None
lock = threading.Lock()

def initialize_engine():
    global engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)

def speak(audio):
    global engine, lock
     # Initialize engine if it hasn't been done already
    if engine is None:
        with lock:
            if engine is None:
                initialize_engine()

     # Use the speech engine to speak the text
    engine.say(audio)
    engine.startLoop(False)
    engine.iterate()
    engine.endLoop()
