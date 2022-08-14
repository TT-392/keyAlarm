import os
import time

class keyboard:
    blocked = False
    def block():
        os.system('xinput float "MfgName Keyboard"')
        keyboard.blocked = True
    def unblock():
        if (keyboard.blocked):
            os.system('xinput reattach "MfgName Keyboard" 3')
            keyboard.blocked = False

