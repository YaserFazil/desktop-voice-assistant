import os
import time

from click import command

MoNo = '7620464305'
command = 'adb shell am start -a android.intent.action.CALL -d tel:+91'+MoNo
# command1 = 'adb shell service call phone 5'  ------ to reject call
# command2 = 'adb shell input keyevent 5' -------------- to receive call

print('calling...')
os.system(command2)
