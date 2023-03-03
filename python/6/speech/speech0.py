# Says hello

import pyttsx3

engine = pyttsx3.init()
newVoiceRate = 145
engine.setProperty("rate", newVoiceRate)
engine.say("hello, world")
engine.runAndWait()
