import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
# To convert voice into text
def takeCommand():
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

if __name__ == '__main__':
    takeCommand()
    speak("Hello My Name Is Indra Juliansyah Putra")