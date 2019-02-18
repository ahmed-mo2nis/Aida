from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tts import tts
import re

def open_firefox():
    tts("OK, opening Firefox")
    webdriver.Firefox()

def check_email():
    un = "YOUR_USER_NAME"
    pw = "YOUR_PASSWORD"
    driver = webdriver.Firefox()
    driver.get("https://mail.protonmail.com/login")  #mail.tutanota.com
    assert "ProtonMail" in driver.title
    element = driver.find_element_by_id("username")
    element.send_keys(un)
    element = driver.find_element_by_id("password")
    element.send_keys(pw)
    element.send_keys(Keys.ENTER)

def search_for(speech_text):
    words_of_message = speech_text.split()
    words_of_message.remove("search")
    cleaned_message = ' '.join(words_of_message)
    driver = webdriver.Firefox()
    driver.get("https://startpage.com/")
    assert "Startpage.com" in driver.title
    element = driver.find_element_by_name("query")
    element.clear()
    element.send_keys(cleaned_message)
    element.send_keys(Keys.ENTER)
    assert "No results found." not in driver.page_source
