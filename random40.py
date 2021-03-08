# importing required module 
from tkinter import *
from threading import *
import time
from gtts import gTTS 
import re
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import pywhatkit
import pyjokes
from googlesearch import search 

r = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def threading(): 
    # Call work function 
    t1=Thread(target=play) 
    t1.start() 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! and Welcome back! Mr. Refat")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! and Welcome back! Mr. Refat")   

    else:
        speak("Good Evening! and Welcome back! Mr. Refat")  

    speak("Sir, I am RANDOM40. Please tell me how may I help you") 


# this module helps to 
# play the converted audio 
import os 

# create tkinter window 
root = Tk() 


# styling the frame which helps to 
# make our background stylish 
frame1 = Frame(root, 
			bg = "lightPink", 
			height = "150") 

# plcae the widget in gui window 
frame1.pack(fill = X) 


frame2 = Frame(root, 
			bg = "lightgreen", 
			height = "750") 
frame2.pack(fill=X) 



# styling the label which show the text 
# in our tkinter window 
label = Label(frame1, text = "Personal Assistant", 
			font = "bold, 30", 
			bg = "lightpink") 

label.place(x = 110, y = 70) 



def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak("Sir you said")
        speak(query)

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def play(): 
    # wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'google search' in query:
            query = query.replace("google search ", "")
            query=query.replace(" ","+");
            url="https://www.google.com/search?q="+query
            chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            chrome_browser.open_new_tab(url)
            # webbrowser.open_new_tab(url)
        
        elif 'go to sleep' in query:
            speak('Shutting down...')
            sys.exit(0)

        elif 'open youtube' in query:
            speak('Opening Youtube...')
            chrome_browser = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            chrome_browser.open_new_tab("youtube.com")
            # webbrowser.open_new_tab("youtube.com")

        elif 'open stack overflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")   

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'suggest app' in query:
            speak('your most used apps are Codeblocks, Microsoft word, Spotify. Do you want to open one?')

        elif 'open code blocks' in query:
            speak('Opening codeblocks sir! Please wait a bit')
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath) 
        
        elif 'open microsoft word' in query:
            speak('Opening word sir! Please wait a bit')
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath) 
        
        elif 'open spotify' in query:
            speak('Opening spotify sir! Please wait a bit')
            codePath = "C:\\Users\\Refat\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath) 
        
        
        


btn = Button(frame2, text = "COMMAND", 
			width = "15", pady = 10, 
			font = "bold, 15", 
			command = threading, bg='yellow') 

btn.place(x = 200, 
		y = 130) 

# give a title 
root.title("Personal Assistant") 



# we can not change the size 
# if you want you can change 
root.geometry("650x550+350+200") 

# start the gui 
# wishMe()

root.after(1000, wishMe) 
root.mainloop() 
