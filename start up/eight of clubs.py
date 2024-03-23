import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.say("eight of clubs")
engine.runAndWait()