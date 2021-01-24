import re
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            reg_ex = re.search('open google and search (.*)', query)
            search_for = query.split("search",1)[1]
            url = 'https://www.google.com/'
            if reg_ex:
                subgoogle = reg_ex.group(1)
                url = url + 'r/' + subgoogle
            speak('Okay!')
            driver = webdriver.Firefox(executable_path='E:\\Software\\geckodriver') #depends which web browser you are using
            driver.get('http://www.google.com')
            search = driver.find_element_by_name('q') # finds search
            search.send_keys(str(search_for)) #sends search keys 
            search.send_keys(Keys.RETURN) #hits enter
        
        elif 'go to sleep' in query:
             speak('Shutting down...')
             sys.exit(0)

        elif 'open youtube' in query:
            speak('Opening Youtube...')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play' in query:
            music_dir = 'D:\\MUSIC\\audio music\\English'
            # D:\MUSIC\audio music\English
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak('Opening codeblocks sir! Please wait a bit')
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)

        elif 'idm' in query:
            speak('Opening internet download manager!')
            codePath = "C:\\Program Files (x86)\\Internet Download Manager\\IDMan.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
