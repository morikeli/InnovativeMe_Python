# Program to change voice of bot to a female.
import pyttsx3 as tts

speaker = tts.init()
voices = speaker.getProperty('voices')
# for loop iterates through properties of the bot.
for voice in voices:
    print(f'ID: {voice.id}')
    print(f'Name: {voice.name}')
    print(f'Gender: {voice.gender}')

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
speaker.setProperty('voice', voice_id)
speaker.setProperty('rate', 170)
speaker.say("Hello Mori. How are you?")
speaker.runAndWait()
