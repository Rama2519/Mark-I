import wikipedia
from variables import *

x = convert(user_input)


def main(command):
    if command[0] == "open" and len(command) == 2:
        command.remove('open')
        command = list_to_string(command)
        filepath = findfile(command, "C:")
        print(filepath)
    # Open Website
    elif command[0] == "open" and command[2] == "website":
        command.remove('open')
        command.remove('website')
        command = list_to_string(command)
        website(command)
    # Open App
    elif command[0] == "open":
        command.remove('open')
        command = list_to_string(command)
        speak_text(opening + command)
        open_app(command)
    # Play my music
    elif command == ['play', 'my', 'music']:
        my_music()
    # Play music
    elif command[0] == "play":
        command.remove("play")
        command = list_to_string(command)
        r1 = sr.Recognizer()
        with sr.Microphone() as source1:
            r1.adjust_for_ambient_noise(source1, duration=0.2)
            speak_text(options)
            print('listening...')
            audio1 = r1.listen(source1)
            user_input1 = [r1.recognize_google(audio1)]
        user_input1 = convert(user_input1)
        speak_text(playing + command)
        if user_input1[0] == "Amazon":
            music_amazon(command)
        else:
            music_yt(command)
    # Wikipedia search
    elif command[0] == "what" or command[0] == "who":
        command = list_to_string(command)
        print(wikipedia.summary(command, sentences=2))
        speak_text(wikipedia.summary(command, sentences=2))
    # Pip install
    elif command[0] == "PIP":
        print('installing...')
        command = list_to_string(command)
        command.lower()
        open_cmd(command)
    else:
        print('none')


main(x)
