# This is a script to mimic customer care service voice message using pyttsx3 (Python's text-to-speech) library.
# The script only works in Windows machines.

import pyttsx3 as tts

def mimic_customer_care_service_teller():
    """
        Safaricom is the largest telcom brand in Kenya.
        This function mimics the voice of their customer care service voice messages.
    """
    speaker = tts.init()
    voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    speaker.setProperty('voice', voice_id)
    speaker.setProperty('rate', 140)
    speaker.setProperty('volume', 0.1)
    speaker.say("Sorry...the mobile subscriber cannot be reached. Please try again later")
    speaker.runAndWait()


if __name__ == '__main__':
    mimic_customer_care_service_teller()
