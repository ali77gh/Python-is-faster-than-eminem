#ememem record
# 16 s

import time
import pyttsx3
    
engine = pyttsx3.init("espeak")

path = './fastpart.txt'
f = open(path, 'r')
rapGod = f.read()

# improve speed
rapGod = rapGod.replace('\n',' ')

print("raping...")

engine.setProperty('rate', 300)  # words per minute
engine.say(rapGod)

start = time.time()
engine.runAndWait()
end = time.time()

print("python: " + str(end-start)[0:4] + "s")
print("eminem: 16s")
