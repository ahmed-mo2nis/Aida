import os
import sys
import speech_recognition as sr

def tts(message):
    #This function takes the message as an argument & converts it to a speech depending on the OS
    if sys.platform == 'linux2':
        tts_engine = 'espeak -ven+f5 '
        return os.system(tts_engine + '"' + message + '"')
    elif sys.platform =='linux':
        tts_engine = 'espeak -ven+f5 '
        return os.system(tts_engine + '"' + message + '"')
