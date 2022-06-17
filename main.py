
# eel gui library
import os
from statistics import mode
import eel

from engine.command import *
from engine.features import *

from engine.config import *

eel.init('www')

if __name__ == "__main__":

    # music_dir = "www\\assets\\audio\\start_sound.mp3"
    # playsound(music_dir)

    @eel.expose
    def StartSound():
        music_dir = "www\\assets\\audio\\start_sound.mp3"
        playsound(music_dir)

    @eel.expose
    def Start():
        # os.system("static/devices.bat")
        eel.AssistantName(ASSISTANT_NAME)
        from engine.features import wish
        wish()
        eel.hideStart()
        eel.init()
        # allCommands()

    eel.start("index.html")
