import speech_recognition as sr
import pyttsx3 as tts

recognizer = sr.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 170)

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            note = recognizer.recognize_google(audio)
            note = note.lower()

            speaker.say(f'Did you say {note}')
            speaker.runAndWait()
            
    except sr.UnknownValueError:
        print('Unknown error')