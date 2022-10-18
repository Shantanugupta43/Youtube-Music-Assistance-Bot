# SHAAN's YOUTUBE ASSISTANT BOT 
# Can process any song recommended by the user using speech recognition and load it on Youtube.
# Install speech_recognition, selenium and pyttsx3 libraries to make it work.
# To start the bot, enter python voicerecognise.py in the command line


# Importing all the python libraries and files for the project to run
import speech_recognition as s      # Library required to understand the voice command given by the user
from voicespeaker import cancelbot  # from voicespeaker.py file importing cancelbot() function
from voicespeaker import *           # importing everything from voicespeaker.py file
from selenium import webdriver       # Importing webdriver from selenium library

from selenium.webdriver.common.keys import Keys    # Importing Keys from selenium.webdriver.common.keys library  
import time  # importing time

from duracheck import *     # importing everything from duracheck.py file




def mic():                                     
    recog = s.Recognizer()                    # Recognises the speech
    
    with s.Microphone() as voiceinput:         # activates Mic on the computer and listens user commands
        txt = recog.listen(voiceinput)
    try:
        txt_recognised = recog.recognize_google(txt)  # processes data from Google Speech Recognition API
        print(txt_recognised)

        if txt_recognised == "cancel":             # if user says cancel after starting the bot or listening to one song it performs 
            cancelbot()                            # actions from cancelbot() function created in voicespeaker.py file which throws a message and shuts it down

        
        
        engine = pyttsx3.init()
        #CHANGING THE SPEAKING RATE
        rate = engine.getProperty('rate')   # collecting info of current speaking rate
        print(rate)                         # printing it
        engine.setProperty('rate',160)      # changing it
        # CHANGING VOICE 
        voices = engine.getProperty('voices')       # collecting info of the current voice
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        engine.say(txt_recognised)                 # takes the recognised text given by the user
        engine.say("playing for you now ... have fun listening!")      # says the message
        engine.runAndWait()

        
        
        driver_path = "C:\Program Files (x86)\chromedriver.exe"  # locates chrome webdriver
        driver = webdriver.Chrome(driver_path)               # uses library and uses driver from the path
        driver.get("https://www.youtube.com/")               # opens Youtube
        time.sleep(3)                                        # task is on hold for certain time (seconds)
        driver.find_element_by_link_text("ACCEPT ALL").click()  # Searches "I AGREE" on the cookie page and clicks it
        time.sleep(1)                                        #task is on hold for certain time (seconds)
        ytsearch= driver.find_element_by_name("search_query")  # Locates search bar on Youtube
        time.sleep(3)                                         #task is on hold for certain time (seconds)
        ytsearch.send_keys(txt_recognised)                    # type's the text recognised by the user 
        time.sleep(3)                                         # task is on hold for certain time (seconds)
        ytsearch.send_keys(Keys.RETURN)                       # Clicks on "enter" such that results are further shown
        time.sleep(5)                                         # task is on hold for certain time (seconds)

        # Xpath for any time frame text shown after performing a youtube search for the first video
        t = driver.find_element_by_xpath("//body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-search[@role='main']/div[@id='container']/ytd-two-column-search-results-renderer[@class='style-scope ytd-search']/div[@id='primary']/ytd-section-list-renderer[@class='style-scope ytd-two-column-search-results-renderer']/div[@id='contents']/ytd-item-section-renderer[@class='style-scope ytd-section-list-renderer']/div[@id='contents']/ytd-video-renderer[1]/div[1]/ytd-thumbnail[1]/a[1]/div[1]/ytd-thumbnail-overlay-time-status-renderer[1]/span[1]").text
        val = sec_convert(t) # takes the time frame in the form of minutes and seconds and converts it to seconds
        strtoint = int(val)  # takes the text (which has been converted to seconds) converts it from String to Integer
        
        
        time.sleep(5)
        # Xpath for the frame after performing a youtube search for the first video and performs click action
        driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]").click()
        
        time.sleep(6)
        driver.refresh()  # Refreshes the browser for the 1st time
        skippingad()      # Importing skippingad() function from voicespeaker.py
        time.sleep(3)
        driver.refresh()   # Refreshes the browser for the 2nd time
        time.sleep(8)
        driver.refresh()   # Refreshes the browser for the 3rd time
        time.sleep(2)
        driver.refresh()   # Refreshes the browser for the 4th time
        
        time.sleep(strtoint) # takes the value and keeps the video on hold till the time it finishes 
        time.sleep(3)   
        
        driver.close()      # closes the browser
        
        
        
        
        nextcancel()   # uses nextcancel() function from voicespeaker.py file
        mic()  # uses mic() function

        

        
        

    except s.UnknownValueError:
        print("")
    except s.RequestError as r:
        print("")




    
        
 

start()  # calls the start() function  
mic() # calls the mic() function
    


       
        
        
        

            
            
        

    
    