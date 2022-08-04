import pyttsx3

engine = pyttsx3.init()


while True:
    answer=input("Enter what you want to say: ")
    engine.say(answer)
    engine.runAndWait()
