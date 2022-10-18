# The file "voicespeaker.py" have functions 
# which enable computer to speak after an action is performed

import pyttsx3 # Imports pyttsx3 library which enables computer to speak

# STARTING SPEECH
def start():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # collecting info of current speaking rate
    print(rate)                        # printing it
    engine.setProperty('rate',160)      # changing it
    voices = engine.getProperty('voices')       # collecting info of the current voice
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    engine.say("Hello Shaan, Welcome to Youtube Music Assistant: which song do you wanna listen to? Can I get the name of it please?")
    engine.runAndWait()
    
# SPEECH AFTER SONG IS FINISHED
def nextcancel():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # collecting info of current speaking rate
    print(rate)                        # printing it
    engine.setProperty('rate',160)       # changing it
    
    voices = engine.getProperty('voices')       # collecting info of the current voice
    engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female
    engine.say("Fancy listening to another song? If yes, can i get the name of it please? To exit the bot say,... cancel")
    engine.runAndWait()

# SAYS SKIPPING AD, LETTING USER KNOW THE BOT IS SKIPPING ADS
def skippingad():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # collecting info of current speaking rate
    print(rate)                        # printing it
    engine.setProperty('rate',160)      # changing it
    voices = engine.getProperty('voices')       # collecting info of the current voice
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
    engine.say("Skipping ads")
    engine.runAndWait()

# IF THE USER SAYS "CANCEL", THE BOT SPEAKS THIS
def cancelbot():
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # collecting info of current speaking rate
    print(rate)                        # printing it
    engine.setProperty('rate',160)       # changing it
    
    voices = engine.getProperty('voices')       # collecting info of the current voice
    engine.setProperty('voice', voices[1].id)  #changing index, changes voices. 1 for female
    engine.say("Bot is shutting down... Hope you have a great day.. Goodbye!")
    engine.runAndWait()
    throwinganerror()    # function throwinganerror() is called

 # FORCEFULLY THROWS AN ERROR WHICH STOPS THE BOT 
def throwinganerror():
    a = Botshutdown
    
    



    




    
    


