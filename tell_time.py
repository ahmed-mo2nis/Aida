from datetime import datetime
from datetime import date
import calendar
import time
from tts import tts

def what_is_the_time():
    tts("The time is: " + datetime.now().strftime("%H:%M:%S"))

def what_is_the_day():
    tts("Today is: " + calendar.day_name[date.today().weekday()] + ". Day number: " + str(date.today().weekday()) + " of the month")

def what_is_the_month():
    tts("We are at the month of: " + calendar.month_name[date.today().weekday()])

def what_is_the_date():
    tts("Today's date is: " + str(date.today()))
