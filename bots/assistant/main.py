from speaker_config import Speaker
from datetime import datetime
import webbrowser as wb
import sys

current_date = datetime.today()
current_time = current_date.strftime('%H:%M')


def greetings():
    print('---'*30)
    print(f'{"BOT says Hi":^80s}')
    Speaker.speaker.say("Hello. I'm Bot what can I do for you?")
    Speaker.speaker.runAndWait()

    print('==='*30)
    print('I can only perform these tasks')
    s = "1.Web search\n2.Tell current time and date"
    print(s)
    print('==='*30)

    try:
        task = int(input('Enter your choice: `1` or `2` or `3`: '))
        choice = [1, 2, 3]
        if task not in choice:
            Speaker.speaker.say("Choice out of range")
            Speaker.speaker.runAndWait()
        else:
            done = False
            while not done:
                if task == 1:
                    search = str(input('Enter what you want to search on the web: '))
                    wb.get().open(f'https://www.google.com/search?q={search}')

                    Speaker.speaker.say("Want to search for anything else?")
                    Speaker.speaker.runAndWait()

                    repeat_task = str(input('Enter your choice: `Yes` or `No`: '))
                    if repeat_task.isdigit() or repeat_task.isnumeric() or repeat_task.isalnum():
                        Speaker.speaker.say("Sorry...Invalid input")
                        Speaker.speaker.runAndWait()
                        print('---'*20)
                        print(":(")
                        sys.exit(1)

                    elif 'no' in repeat_task.lower():
                        done = True
                        Speaker.speaker.say("Sad to see you leave... Goodbye. See you soon")
                        Speaker.speaker.runAndWait()
                else:
                    Speaker.speaker.say(f"It's now {current_time}. Current date: {current_date.strftime('%A %dth-%B-%Y')}")
                    Speaker.speaker.runAndWait()
                    done = True
    
    except ValueError:
        Speaker.speaker.say("Invalid input. Type 1 or 2 or 3")
        Speaker.speaker.runAndWait()




if __name__ == '__main__':
    greetings()
