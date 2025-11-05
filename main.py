import datetime
import os
import subprocess #For opening apps in windows
from time import strftime
import openai
from config import apikey
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import random
from google import genai

engine = pyttsx3.init()
engine.say(" good morning Sir , how may I help you ")
engine.runAndWait()



def ai(prompt):
    key = "AIzaSyD8I1UViqZFEOfMpF1XNRA2p5Ak3U1ne5I"


    client = genai.Client(api_key=key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )

    #todo: wrap this inside of a try catch block
    print(response.text)
    engine.say(response.text)
    engine.runAndWait()


def takeCommand():
    """Capture voice input from the user."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = r.listen(source)
        try:
           query = r.recognize_google(audio, language="en-in")
           print(f"User Said: {query}")
           return query
        except sr.UnknownValueError:
           print("Sorry, I could not understand the audio.")
           return "I could not understand."
        except sr.RequestError:
           print("Could not request results, check your internet connection.")
           return "Request error."

if __name__ == '__main__':
    print('PyCharm')
    while True:
        print("Welcome to J.A.R.V.I.S Listening Rishi ")
        query = takeCommand()
        #todo:Add more sites
        sites = [["youtube","https://www.youtube.com"],["wikipedia", "https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                engine.say(f"Opening {site[0]} madam...")
                webbrowser.open(site[1])
            #todo : Add a feature to play a specific song
            if "Open song".lower() in query.lower():
                musicPath = r"C:\Users\Admin\Desktop\PyCharm Community Edition 2024.3.3\music.mp3"
                os.startfile(musicPath)  # Works on Windows
            elif "the time".lower() in query.lower():
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                engine.say(f"Sir the time is {hour} bajjkkkeee {min} minutes")
                engine.runAndWait()
                print(f"the time is:{hour}:{min}")
                                                  # Open applications (Windows-specific)
            elif "open notepad".lower() in query.lower():
                subprocess.Popen(["notepad.exe"])

            elif "open calculator".lower() in query.lower():
                subprocess.Popen("calc.exe")

            elif "open command prompt".lower() in query.lower():
                subprocess.Popen("cmd.exe")
            elif "using AI".lower() in query.lower():
                ai(prompt=query)


        #if query:
         #  engine.say(query)
          # engine.runAndWait()
