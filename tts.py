from gtts import gTTS
import sys

def mainfunc():
    print("[1] if want to read from script.txt\n[2] if you want to write script to console.\n\nNote that output file will be in the same directory as script.\n")
    option = int(input())
    if option == 1:
        with open('script.txt', 'r') as f:
            tts = gTTS(f.read())
            tts.save('(t)script.mp3')
        print("(t) Indicates that file is generated (read) from text file.")
        input("Run Successfully Press any key to exit.")
    elif option == 2:
        print("Input script: ")
        script = input()
        tts = gTTS(script)
        tts.save('(c)script.mp3')
        print("(c) Indicates that file is generated (read) from console.")
        input("Run Successfully Press any key to exit.")
    else:
        print("Please enter a valid input...")
        mainfunc()

if __name__ == "__main__":
    mainfunc()