from bs4 import BeautifulSoup
from tts import tts
import requests

def forecast(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove("weather")
    cleaned_message = ' '.replace(" ", "-").join(words_of_message)

    try:
        result = requests.get("https://www.weather-forecast.com/locations/"+cleaned_message+"/forecasts/latest")
        soup = BeautifulSoup(result.content, "lxml")
        forecasts = soup.find_all("p")[1:2]
        for forecast in forecasts:
            tts(forecast.text)

    except:
        tts("Something went wrong, please try again")
