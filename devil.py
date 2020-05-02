#!/usr/bin/python3
import os
import random
import datetime
import time
from gtts import gTTS
from playsound import playsound
import requests

url = "https://api.thevirustracker.com/free-api?global=stats" # API 1
url2 = "https://api.covid19api.com/summary" # API 2
sounds = os.listdir('sounds')
sounds.remove('wel.mp3')

def tellmenews(number):
    msg = "Meanwhile... " + number + "... more people died... due to Corona Virus."
    tts = gTTS(text = msg, lang='en')
    tts.save('tmp/msg.mp3')
    playsound("sounds/" + random.choice(sounds))
    time.sleep(2)
    playsound("tmp/msg.mp3")
    os.remove('tmp/msg.mp3')

deaths_ = 0

if __name__=="__main__":
    playsound("sounds/wel.mp3")

    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": "
        try:
            response = requests.get(url).json()
            deaths = response["results"][0]["total_deaths"]
        except:
            print(timestamp + "Something wrong with API 1, Using API 2")

            try:
                response = requests.get(url2).json()
                deaths = response['Global']['TotalDeaths']
            except:
                print(timestamp + "No API is working wait for few minutes")


        if deaths_ < deaths:
            print(timestamp + "Yo! Got an update")
            tellmenews(str(deaths-deaths_))
            deaths_ = deaths
        else:
            print(timestamp + "No new update right now")


        time.sleep(120)
