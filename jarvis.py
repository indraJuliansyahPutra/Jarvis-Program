import datetime
import pyttsx3
import speech_recognition as sr
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
# To convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
        
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour <= 12:
        speak('Good Morning')
    elif hour > 12 and hour <= 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    
    speak('I am Jarvis sir, Please tell me how can i help you ?')

def sendEmail(to, content):
    server = smtplib.SMTP('smt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendemail('your email id', to, content)
    server.close()

if __name__ == '__main__':
    wish()
    while True:
    #if 1:
        query = takecommand().lower()
        #query = "Jarvis, open command prompt please"
        #speak(query)
        
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            
        elif "open wps" in query:
            npath = "C:\\Users\\axioo\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe"
            os.startfile(npath)
            
        elif "open command prompt" in query:
            os.system("start cmd")
            
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif "play music" in query:
            music_dir = "D:\\Music\\Best Music Ever"
            songs = os.listdir(music_dir)
            #random_song = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3') or song.endswith('.mp4') or song.endswith('.m4a'):
                    os.startfile(os.path.join(music_dir, song))
                    
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your Ip Address is {ip}")
            
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            speak(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
        elif "open google" in query:
            speak('Sir, what should i search on google')
            cm = takecommand().lower
            #cm = "Argentina"
            speak(f"Search with keyword {cm}")
            search_url = f"https://www.google.com/search?q={cm}"
            webbrowser.open(search_url)
            
        elif "send message"  in query:
            kit.sendwhatmsg("+6281541114284", "this is testin protocol", 22, 25)
            
        elif "play song on youtube" in query:
            speak("What song should i play on youtube....")
            #lagu = "Jejak Pesawat"
            query = takecommand().lower()
            speak(f"{query} will play on youtube")
            kit.playonyt(query)
            
        elif "email to presiden" in query:
            try:
                speak("What should i say?")
                #content = takecommand().lower()
                content = "This is an example"
                to = "presidenri2054@gmail.com"
                sendEmail(to, content)
            
            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to sent this email to president")
                
        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day")
            sys.exit()
                
        speak("Sir, do you have any other work")