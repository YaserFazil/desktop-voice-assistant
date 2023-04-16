
# eel gui library
from enum import Flag
import os
from statistics import mode
import eel
import subprocess
from engine.command import *
from engine.features import *
from authenticate.recoganize import AuthenticateFace
from engine.config import *
import cv2

eel.init('www')


if __name__ == "__main__":

    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

    @eel.expose
    def StartSound():
        music_dir = "www\\assets\\audio\\start_sound.mp3"
        playsound(music_dir)

    @eel.expose
    def Start():
        subprocess.call([r'static\\devices.bat'])
        # os.system("static\\devices.bat")
        eel.AssistantName(ASSISTANT_NAME)

        from engine.features import auth_protocol
        auth_protocol()
        flag = AuthenticateFace()
        # flag =1 #skip face authenticate
        print(flag)
        if flag == 1:

            eel.hideFaceAuth()
            speak("Face authentication successfull")
            eel.hideFaceAuthSuccess()

            from engine.features import wish
            wish()
            eel.hideStart()
            eel.init()
        else:
            speak("authentication fail")

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start("index.html", mode=None,
              host='localhost',
              block=True)
