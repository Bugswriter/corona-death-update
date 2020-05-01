import os
import random
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
        try:
            response = requests.get(url).json()
            deaths = response["results"]["total_deaths"]
        except:
            print("Something wrong with API 1")
            print("Using API 2...")

        try:
            response = requests.get(url2).json()
            deaths = response['Global']['TotalDeaths']
        except:
            print("No API is working wait for few minutes")


        if deaths_ < deaths:
            print("Yo! Got an update")
            tellmenews(str(deaths-deaths_))
            deaths_ = deaths


        time.sleep(120)
