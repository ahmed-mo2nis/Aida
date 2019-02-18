#!/usr/bin/env python3
from deepspeech import Model
import scipy.io.wavfile as wav
import speech_recognition as sr
import sys
import os

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something !")
    audio = r.listen(source)
    # message = r.recognize_sphinx(audio)       #Comment this line if you wish to use CMU pocket sphinx speech recognition instead
with open("recording.wav", "wb") as f:
    f.write(audio.get_wav_data())

#Comment the following part if you wish to use another speech recognition module

os.system("deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio recording.wav >> data.txt")
f = open("data.txt", "r")
if f.mode == "r":
    message = f.read()
    print("Deep Speech Thinks You Said: " + message)
    tts_engine = 'espeak '
    os.system(tts_engine + '"' + message + '"')
    f = open("data.txt", "w+")   #+w means write/create. +a means append/create. r means read
    f.write("")                  #delete contents of text file
    f.close()
    os.remove("recording.wav")   #delete wav file

#Uncomment this part if you intend to recognize speech using CMU Pocket Sphinx Speech Recognition instead of Deep Speech

# try:
#     print("Pocket Sphinx thinks you said : " + message)
#     tts_engine = 'espeak '
#     os.system(tts_engine + '"' + message + '"')
#
# except sr.UnknownValueError:
#     print("Pocket Sphinx couldn't understand audio")
#
# #Uncomment this part ONLY if you intend to use an online speech recognition above (for example: r.recognize_google) BUT IT'S INSECURE !
#
# except sr.RequestError as e:
#     print("Couldn't request results from the internet; {0}".format(e))
