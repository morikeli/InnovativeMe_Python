# Code block to change voice of bot to a female.
import pyttsx3 as tts

speaker = tts.init()
voices = speaker.getProperty('voices')

# iterate through properties of the bot.
for voice in voices:
    print(f'ID: {voice.id}')
    print(f'Name: {voice.name}')
    print(f'Gender: {voice.gender}')

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
speaker.setProperty('voice', voice_id)
speaker.setProperty('rate', 170)    # speed rate (how fast the bot talks)
speaker.say("Hello there. How are you?")
speaker.runAndWait()
