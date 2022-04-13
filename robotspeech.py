import pyttsx3 as tts


def robot():
    tts.speak("Hello, what's your name? ")
    user = str(input('Enter your name: '))
    speaker = tts.init()
    voices = speaker.getProperty('voices')

    speaker.setProperty('rate', 150)
    tts.speak(f'Hello {user}')
    speaker.runAndWait()

robot()
