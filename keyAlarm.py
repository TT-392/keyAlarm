# import needed modules
import os
from datetime import datetime
import pyxhook
from pynotifier import Notification
import time
from blockKeyboard import *

maxCount = 300
def notify_send(title, description) :
    Notification(
        title=title,
        description=description,
        icon_path='/home/user/Downloads/745460.png',
        duration=3,                                   # Duration in seconds
        urgency='critical'
    ).send()


# main function
# specify the name of the file (can be changed )
log_file = f'{os.getcwd()}/{datetime.now().strftime("%d-%m-%Y|%H:%M")}.log'

# the logging function with {event parm}
def keyDown(event):
    keyDown.count += 1
    #print(keyDown.count);
keyDown.count = 0;

# the logging function with {event parm}
def keyUp(event):
    keyUp.count += 1
    #print(keyUp.count)

    if (keyUp.count > maxCount):
        notify_send("TYPING WARNING", str(keyUp.count) + " keystrokes");

    if (keyUp.count > maxCount + 100):
        keyboard.block();

    print(maxCount-keyUp.count);

keyUp.count = 0;



# create a hook manager object
new_hook = pyxhook.HookManager()
new_hook.KeyDown = keyDown
new_hook.KeyUp = keyUp

new_hook.HookKeyboard()  # set the hook

try:
    new_hook.start()  # start the hook
except KeyboardInterrupt:
    # User cancelled from command line.
    pass
except Exception as ex:
    # Write exceptions to the log file, for analysis later.
    msg = f"Error while catching events:\n  {ex}"
    pyxhook.print_err(msg)
    with open(log_file, "a") as f:
        f.write(f"\n{msg}")

start_time = time.time()
interval = 1

while 1:
    time.sleep(1)
    if (keyUp.count == 0):
        keyboard.unblock();

    if (keyUp.count > 0):
        keyUp.count -= 1
    print(maxCount-keyUp.count);

