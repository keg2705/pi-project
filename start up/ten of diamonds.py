import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say("ten of diamonds")
engine.runAndWait()