# importing required module 
from tkinter import *
# from tkinter.ttk import *
from threading import *
import time
from gtts import gTTS 
import re
import os 
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
import smtplib
import add_app
import myInfo
import contacts
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

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    fh=open('password.txt')
        password=fh.read()
    password=
    server.login('kazishaharin@gmail.com',password)
    server.sendmail('kazishaharin@gmail.com',to,content)
    server.close()

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
            try:
              fh=open('chromeloc.txt')
              codePath=fh.read()
              print(codePath)
              fh.close()
              chrome_browser = webbrowser.get(codePath)
              chrome_browser.open_new_tab(url)
            except Exception as e:
              print("Error:",type(e))
              speak('Google Chrome not found! Update Google Chrome location')
        
        elif 'go to sleep' in query:
            speak('Shutting down...')
            sys.exit(0)


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'suggest app' in query:
            speak('your most used apps are Codeblocks, Microsoft word, Spotify. Do you want to open one?')
        elif 'open' in query:
          query=query.replace('open ','')
          if query=='youtube':
            try:
              fh=open('chromeloc.txt')
              codePath=fh.read()
              # chrome location should be added in forward slash instead of backward slash
              print(codePath)
              fh.close()
              speak('Opening Youtube...')
              chrome_browser = webbrowser.get(codePath)
              chrome_browser.open_new_tab("youtube.com")
            except Exception as e:
              print("Error:",type(e))
              speak('Google Chrome not found! Update Google Chrome location')
          else:
            print(query)
            name=query+'.txt'
            try:
              fh=open(name)
              codePath=fh.read()
              print(codePath)
              speak('Opening '+query+' sir! Please wait a bit')
              os.startfile(codePath)
              fh.close()
            except Exception as e:
              print("Error:",type(e))
              speak('no such application found!')
        
        elif 'send email to' in query:
            query=query.replace('send email to ','') 
            name=query+'.txt'
            try:
              fh=open(name)
              to=fh.read()
              fh.close()
              try:
                speak('what should i say?')
                content=takeCommand()
                print(to)
                sendEmail(to,content)
                speak('email has been sent!')
              except Exception as e:
                print(e)
                speak('sorry i am not able to send this email due to technical difficulties')
            except Exception as e:
              print(e)
              speak('no contact named '+query+' is found!')

        

# create tkinter window 
root = Tk() 


# styling the frame which helps to 
# make our background stylish 
frame1 = Frame(root, bg = "lightPink", height = "150") 

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

btn = Button(frame2, text = "COMMAND", 
			width = "15", pady = 10, 
			font = "bold, 11", 
			command = threading, bg='yellow') 

btn.place(x = 240, 
		y = 130) 

btn2 = Button(frame2, text = "MY INFO", 
			width = "15", pady = 10, 
			font = "bold, 11", 
			command = myInfo.openNewWindow, bg='yellow') 

btn2.place(x = 240, 
		y = 180) 

btn3 = Button(frame2, text = "ADD APP", 
			width = "15", pady = 10, 
			font = "bold, 11", 
			command = add_app.openNewWindow, bg='yellow') 

btn3.place(x = 240, 
		y = 230) 

btn4 = Button(frame2, text = "ADD CONTACT", 
			width = "15", pady = 10, 
			font = "bold, 11", 
			command = contacts.openNewWindow, bg='yellow') 

btn4.place(x = 240, 
		y = 280) 

# give a title 
root.title("Personal Assistant") 



# we can not change the size 
# if you want you can change 
root.geometry("650x550+350+200") 

# start the gui 
# wishMe()

root.after(1000, wishMe) 
root.mainloop() 
