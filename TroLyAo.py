import speech_recognition
import pyttsx3
from datetime import date,datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

user = "Trang"
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""


    if you == "":
        robot_brain = "I Don't understand"
    elif "hello" in you:
        robot_brain = "Hello "+user
    elif "bye" in you:
        robot_brain = "Bye "+user
        robot_mouth.say(robot_brain)
        print(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "my birthday" in you:
        robot_brain = "Your birthday is August 6, 1995"
    elif "does she love me" in you:
        robot_brain = "yes, she love you"
    else:
        robot_brain = "Good Day"


    voices = robot_mouth.getProperty('voices')
    robot_mouth.setProperty('voice', voices[1].id)

    robot_mouth.say(robot_brain)
    print(robot_brain)
    robot_mouth.runAndWait()