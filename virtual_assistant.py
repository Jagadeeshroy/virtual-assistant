import speech_recognition as sr
from gtts import gTTS
import playsound
import time
from time import ctime
import os

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio = r.listen(source, phrase_time_limit = 5)
    data = ""
    try:
        data = r.recognize_google(audio, language='en-US')
        print("You said:" +data)
    except sr.UnknownValueError:
        print("I cant hear you")
    except sr.RequestError as e:
        print("Request failed")
    return data

def respond(string):
    print(string)
    tts = gTTS(text=string, lang = "en")
    tts.save("speech.mp3")
    playsound.playsound("speech.mp3")
    os.remove("speech.mp3")

def voice_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well")

    if "time" in data:
        listening = True
        respond(ctime())

    if "stop" in data:
        listening = False
        print("listening stopped")
        respond("see you jagadeesh")

time.sleep(2)
respond("hello jagadeesh, what can i do for you")
listening = True
while listening == True:
    data = listen()
    listening = voice_assistant(data)
    
    
