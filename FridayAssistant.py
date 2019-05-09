#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
import pyttsx3
import webbrowser
import sys
import subprocess
import winshell

engine = pyttsx3.init() 


def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def friday(data):

    if "how are you" in data:
        speak("I am fine")

    elif "time" in data:
        speak(ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Megha, I will show you where " + location + " is.")
        webbrowser.open('https://www.google.nl/maps/place/'+location)

    elif "Google" in data:
        data = data.split(" ")
        datum = data[1:(len(data))]
        datum1= "+".join(datum)
        speak("Hold on Megha, searching results for " + " ".join(datum))
        webbrowser.open('https://www.google.com/search?q='+datum1)

    elif "open Notepad" in data:
        speak("Hold on Megha, Opening Notepad++ for you")
        subprocess.call("C:/Program Files (x86)/Notepad++/notepad++.exe")

    elif "empty recycle bin" in data:
        speak("Deleting all files in recycle bin")
        winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=False)

    elif "play" in data:
        data = data.split(" ")
        datum = data[1:(len(data))]
        datum1= "+".join(datum)
        speak("Hold on Megha, showing you the videos of " + " ".join(datum))
        webbrowser.open('https://www.youtube.com/results?search_query='+datum1)

    elif "exit" in data:
        speak("Bye Megha. I hate Thanos and I miss Tony")
        exit()
        

# initialization
time.sleep(2)
speak("Hi Megha, I am Friday, what can I do for you today?")
while 1:
    data = recordAudio()
    friday(data)
