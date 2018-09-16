import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser

# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='es')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)

    data = ""

    try:
        data = r.recognize_google(audio)
        print("Has dicho: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition no te pudo entender")
    except sr.RequestError as e:
        print("No se ha obtenido respuesta desde los servicios de Google Speech Recognition: " + e)

    return data

def jarvis(data):
    if "hola" in data:
        speak("Hola, Joaquín. ¿Qué puedo hacer por ti?")
    
    if "que hora es" in data:
        speak(ctime())

    if "donde esta" in data:
        data = data.split(" ")
        location = data[2]
        speak("Espera Joaquín, te voy a enseñar dónde está " + location + ".")
        webbrowser.get(chrome_path).open("https://www.google.nl/maps/place/" + location + "/&amp;")

time.sleep(2)
speak("En qué puedo ayudarte?")

while 1:
    data = recordAudio()
    jarvis(data)