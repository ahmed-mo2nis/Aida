import os
from brain import brain

#Functioning Variables
home = os.path.expanduser("~")
music_path = os.path.join(home, "Music")

user_template = "USER : {0}"
bot_template = "AIDA : {0}"

def send_message():
    speech_text = input(bot_template.format("What Can I Do For You ? "))
    print(user_template.format(speech_text))
    brain(speech_text, music_path)

while True:
    send_message()
