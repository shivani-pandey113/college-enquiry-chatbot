import pyttsx3
  
# Initialize the converter
converter = pyttsx3.init()
  
# Set properties before adding
# Things to say
  
# Sets speed percent 
# Can be more than 100
converter.setProperty('rate', 140)
# Set volume 0-1
converter.setProperty('volume', 2)
voices = converter.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
converter.setProperty('voice', voices[1].id) 
  
# Queue the entered text 
# There will be a pause between
# each one like a pause in 
# a sentence
converter.say("hello")
converter.say("I'm also a geek")
  
# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()