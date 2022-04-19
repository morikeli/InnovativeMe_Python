import pyttsx3 as tts

speaker = tts.init()
voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
speaker.setProperty('voice', voice_id)
speaker.setProperty('rate', 140)
speaker.setProperty('volume', 0.1)
speaker.say("Sorry...the mobile subscriber cannot be reached. Please try again later")
speaker.runAndWait()
