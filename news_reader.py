from bs4 import BeautifulSoup   #module for formatting the retrieved page
from tts import tts
import requests

def which_news_general():
    tts("Political or Financial or Sports ?")

def which_news_political():
    tts("Which do you want ? BBC ? CNN ? Reuters ? CBS ? Washington Post ? The Guardian ?")

def bbc_news():
    result = requests.get("https://www.bbc.com/news/world")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)

def cnn_news():
    result = requests.get("https://edition.cnn.com/world")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)

def reuters_news():
    result = requests.get("https://www.reuters.com/news/archive/worldNews")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)

def the_guardian():
    result = requests.get("https://www.theguardian.com/world")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)

def cbs_news():
    result = requests.get("https://www.cbsnews.com/world/")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)

def washington_post():
    result = requests.get("https://www.washingtonpost.com/world/")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)

def financial_news():
    result = requests.get("https://www.reuters.com/finance")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)

def bbc_sports():
    result = requests.get("https://www.bbc.co.uk/sport")
    soup = BeautifulSoup(result.content, "lxml")
    headlines = soup.find_all("h3")[:5]
    for headline in headlines:
        tts(headline.text)
