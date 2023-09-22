import speech_recognition as sr
import pyttsx3 as tts
import sys

commands = {
    "greetings": ['Hello', 'Hi', 'How are you', 'What\'s up?'],
    "responses": ['Hi there? What can I do for you?', ],
    "quit": ['Goodbye', ]
}

recognizer = sr.Recognizer()
speaker = tts.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

speaker.setProperty('voice', voice_id)
speaker.setProperty('rate', 170)
speaker.say('Hello, what\'s your name?')
speaker.runAndWait()


def user_response():
    with sr.Microphone() as response:
        audio = recognizer.listen(response)
        bot = recognizer.recognize_sphinx(audio)
        bot = bot.lower()
    speaker.say(f'Hello {bot}')
    speaker.runAndWait()


user_response()

while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            response = recognizer.recognize_google(audio)
            response = response.lower()

            if 'goodbye' in response or 'bye' in response:
                speaker.say(f'Goodbye . Have a blessed day.')
                speaker.runAndWait()
                sys.exit()
    except sr.RequestError as e:
        print('Could not process result: {0}'.format(e))
    except sr.UnknownValueError:
        speaker.say("Sorry. I did not understand you. Come up again.")
        speaker.runAndWait()

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            audio = recognizer.listen(mic)
            response = recognizer.recognize_google(audio)
            response = response.lower()
            speaker.say(f'Now I can hear you... Did you say {response}')
            speaker.runAndWait()
            if ('goodbye' in response or 'bye' in response) and 'yes' in response:
                speaker.say("Goodbye. Have a lovely day.")
                speaker.runAndWait()
                sys.exit()

