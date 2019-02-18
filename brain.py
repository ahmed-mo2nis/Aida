import general_conversations, tell_time, wiki, news_reader, browse, sleep, audio_player, notes, weather
from tts import tts
import os

def brain(speech_text, music_path):
    def check_message(check):
        #This function checks if the items in the list (specified in the argument) are presented in the user's input speech (i.e. keywords)
        words_of_message = speech_text.split()
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False

    if check_message(["who", "are", "you"]):
        general_conversations.who_are_you()
    elif check_message(["how", "i", "look"]) or check_message(["how", "am", "i"]):
        general_conversations.how_am_i()
    elif check_message(["tell", "joke"]):
        general_conversations.tell_joke()
    elif check_message(["who", "am", "i"]):
        general_conversations.who_am_i()
    elif check_message(["where", "born"]):
        general_conversations.where_born()
    elif check_message(["how", "are", "you"]):
        general_conversations.how_are_you()
    elif check_message(["aida"]):
        general_conversations.awake()
    elif check_message(["what", "can", "you", "do"]):
        general_conversations.skills_list()
    elif check_message(["time"]):
        tell_time.what_is_the_time()
    elif check_message(["day"]):
        tell_time.what_is_the_day()
    elif check_message(["month"]):
        tell_time.what_is_the_month()
    elif check_message(["date"]):
        tell_time.what_is_the_date()
    elif check_message(["wikipedia"]):
        wiki.define_subject(speech_text)
    elif check_message(["news"]):
        news_reader.which_news_general()
    elif check_message(["political"]):
        news_reader.which_news_political()
    elif check_message(["bbc"]):
        news_reader.bbc_news()
    elif check_message(["cnn"]):
        news_reader.cnn_news()
    elif check_message(["reuters"]):
        news_reader.reuters_news()
    elif check_message(["the", "guardian"]):
        news_reader.the_guardian()
    elif check_message(["cbs"]):
        news_reader.cbs_news()
    elif check_message(["washington", "post"]):
        news_reader.washington_post()
    elif check_message(["finance"]) or check_message(["financial"]):
        news_reader.financial_news()
    elif check_message(["sports"]) or check_message(["sport"]):
        news_reader.bbc_sports()
    elif check_message(["weather"]):
        weather.forecast(speech_text)
    elif check_message(["open", "firefox"]):
        browse.open_firefox()
    elif check_message(["check", "email"]):
        browse.check_email()
    elif check_message(["search"]):
        browse.search_for(speech_text)
    elif check_message(["sleep"]):
        sleep.go_to_sleep()
    elif check_message(["shutdown"]) or check_message(["turn", "off"]):
        sleep.shutdown()
    elif check_message(["restart"]):
        sleep.restart()
    elif check_message(["play", "music"]) or check_message(["music"]):
        audio_player.play_random(music_path)
    elif check_message(["play"]):
        audio_player.play_specific_music(speech_text, music_path)
    elif check_message(["shuffle", "music"]) or check_message(["mix", "music"]):
        audio_player.play_shuffle(music_path)
    elif check_message(["note"]):
        notes.take_notes(speech_text)
    elif check_message(["all", "notes"]) or check_message(["show", "notes"]) or check_message(["read", "notes"]):
        notes.show_all_notes()
    elif check_message(["delete", "notes"]) or check_message(["erase", "notes"]):
        notes.delete_all_notes()
    elif check_message(["text", "mode"]):
        tts("Now Entering Text Mode")
        os.system("python3 bot.py")
    elif check_message(["voice", "mode"]):
        tts("Now Returning To Voice Mode")
        os.system("python3 index.py")
    else:
        general_conversations.undefined()
