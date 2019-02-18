import random
from tts import tts

def who_are_you():
    messages = ["I'm Aida, your personal assistant", "Aida, I thought I told you before", "My Name is Aida and I'm a personal assistant"]
    tts(random.choice(messages))

def how_am_i():
    replies = ["You Seem Nice", "A Good Person", "You Sound Kind"]
    tts(random.choice(replies))

def skills_list():
    tts("I can take notes for you, read the latest news headlines, play audio files on your computer, tell you the time & weather outside, gather information about anything from Wikipedia, search for anything online, check your e-mail & open Firefox")

def tell_joke():
    jokes = ["I'm afraid I'm not that funny", "Jokes are dead, look at memes instead", "No, I always forget the punch line"]
    tts(random.choice(jokes))

def who_am_i():
    insights = ["You sound like a nice person. I wish you all the best.", "Is that a philosophical question or do you suffer from amnesia?", "Obviously you are my user!"]
    tts(random.choice(insights))

def where_born():
    answers = ["I wasn't exactly born. I'm a computer program remember?", "Technically inside a computer", "Computer programs aren't born, they are written by programmers"]
    tts(random.choice(answers))

def how_are_you():
    feelings = ["I'm fine, thanks for asking", "I'm OK", "Having A Great Day So Far!"]
    tts(random.choice(feelings))

def awake():
    responses = ["How Can I Help You ?", "Is There Something I Can Do For You ?", "Need Help With Something ?"]
    tts(random.choice(responses))

def undefined():
    print("Aida couldn't understand audio")
