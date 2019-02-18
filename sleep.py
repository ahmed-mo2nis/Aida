import os
import random
from tts import tts

def go_to_sleep():
    sleeping = ["Goodbye for now!", "See you later!", "Untill next time!"]
    tts(random.choice(sleeping))
    os.system("pkill -9 python3")

def shutdown():
    shutting = ["Goodbye for now!", "See you later!", "Untill next time!"]
    tts(random.choice(shutting))
    os.system("shutdown -h now")

def restart():
    restarting = ["Goodbye for now!", "See you later!", "Untill next time!"]
    tts(random.choice(restarting))
    os.system("reboot")
