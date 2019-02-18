#!/usr/bin/env python3
import scipy.io.wavfile as wav
import speech_recognition as sr
import os
import sys
from deepspeech import Model
from tts import tts
from brain import brain

#Functioning Variables
home = os.path.expanduser("~")
music_path = os.path.join(home, "Music")

def main():
    #Obtain audio from the microphone and record it to a wav file
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm Listening!")
        audio = r.listen(source)
        with open("recording.wav", "wb") as f:
            f.write(audio.get_wav_data())

    #Comment the following part if you wish to use another speech recognition module

    try:
        os.system("deepspeech --model models/output_graph.pbmm --alphabet models/alphabet.txt --lm models/lm.binary --trie models/trie --audio recording.wav >> data.txt")
        f = open("data.txt", "r")
        if f.mode == "r":
            speech_text = f.read()
            print("Aida thinks you said: " + speech_text)
            f = open("data.txt", "w+")   #+w means write/create. +a means append/create. r means read
            f.write("")                 #delete contents of text file
            f.close()
            os.remove("recording.wav")  #delete wav file

    #Uncomment this part if you intend to recognize speech using CMU Pocket Sphinx Speech Recognition instead of Deep Speech

    # try:
    #     speech_text = r.recognize_sphinx(audio).lower().replace(".","")
    #     print("Aida thinks you said : " + speech_text +"'")

    except sr.UnknownValueError:
        print("Aida couldn't understand audio")

    #Uncomment this part ONLY if you intend to use an online speech recognition above (for example: r.recognize_google) BUT IT'S INSECURE !

    # except sr.RequestError as e:
    #     print("Couldn't request results from the internet; {0}".format(e))

    brain(speech_text, music_path)

while True:
    main()
