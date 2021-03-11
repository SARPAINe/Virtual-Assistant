from tkinter import *
# importing required module 
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
import smtplib
import add_app
from googlesearch import search 

r = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def save():
    print(entry1.get())
    print(entry3.get())

    fh=open('email.txt','w')
    fh.write(entry1.get())
    fh.close()

    fh=open('password.txt','w')
    fh.write(entry2.get())
    fh.close()

    fh=open('chromeloc.txt','w')
    loc=entry3.get()+" %s"
    fh.write(loc)
    fh.close()

    speak('information saved!')


def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Tk()
  
    frame1 = Frame(newWindow, bg = "lightPink", height = "150") 

    # plcae the widget in gui window 
    frame1.pack(fill = X) 


    frame2 = Frame(newWindow, 
          bg = "lightgreen", 
          height = "750") 
    frame2.pack(fill=X) 



    # styling the label which show the text 
    # in our tkinter window 
    label = Label(frame1, text = "Personal Assistant", 
          font = "bold, 30", 
          bg = "lightpink") 

    label.place(x = 110, y = 70) 

    label1=Label(frame2, text="Email", font="bold, 11")
    label1.place(x=80,y=52)
    global entry1
    entry1 = Entry(frame2, width = 20,  
              bd = 4, font = 11) 
  
    entry1.place(x = 240, y = 52) 

    label2=Label(frame2, text="Email Password", font="bold, 11")
    label2.place(x=80,y=82)
    
    global entry2
    entry2 = Entry(frame2, width = 20,  
              bd = 4, font = 11,show="*") 
  
    entry2.place(x = 240, y = 82)

    label3=Label(frame2, text="Chrome location", font="bold, 11")
    label3.place(x=80,y=112)
    
    global entry3
    entry3 = Entry(frame2, width = 20,  
              bd = 4, font = 11) 
  
    entry3.place(x = 240, y = 112)

    btn = Button(frame2, text = "SAVE", 
			width = "10", pady = 10, 
			font = "bold, 11", 
			command = save, bg='yellow') 

    btn.place(x = 240, y = 150)

    newWindow.title("My Information") 



    # we can not change the size 
    # if you want you can change 
    newWindow.geometry("650x550+350+200") 

