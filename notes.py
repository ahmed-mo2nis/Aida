from datetime import datetime
from tts import tts

def take_notes(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove("note")
    cleaned_message = ' '.join(words_of_message)
    f = open("notes.txt", "a+")
    f.write("'" + cleaned_message + "'" + " - note taken at: " + datetime.strftime(datetime.now(), "%d-%m-%y") + "\n")
    f.close()
    tts("Your note has been saved")

def show_all_notes():
    tts("Your notes are as follows: ")
    f = open("notes.txt", "r")
    if f.mode == "r":
        contents = f.read()
        tts(contents)
    f.close()

def delete_all_notes():
    f = open("notes.txt", "w+")   #+w means write/create. +a means append/create. r means read
    f.write("")
    f.close()
    tts("All notes have been deleted")
