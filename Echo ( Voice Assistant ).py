import os
import sys
sys.path.append('/MyModuleForVoice/')
import MyModuleForVoice
from MyModuleForVoice.VoiceModule import *

instruction()
print()
choice=int(input("Enter 1 for text based communication\nEnter 2 for voice based communication\n\nEnter Your Choice = "))
if choice!=1 and choice!=2 :
    print("Please Enter a valid choice")
    exit() 
os.system('cls')

print()
greet()
help()
print()

while True :

    if choice==1 :
        speak("Please Enter Your command")
        text=input("Please Enter your command = ")    
    
    else :
        speak("Please Enter Your command")
        text=listen()
        print("USER : ",text)
    
    l=extract_numbers(text)
    count=0

    if "WIKIPEDIA" in text.upper() and "SEARCH" in text.upper() :
        wiki(text)
        count+=1

    elif "OPEN" in text.upper() and "YOUTUBE" in text.upper() :
        open_youtube()
        count+=1

    elif "OPEN" in text.upper() and "ADOBE" in text.upper() :
        adobe(text)
        count+=1

    elif "OPEN" in text.upper() and "GOOGLE" in text.upper() :
        open_google()
        count+=1
    
    elif ("OPEN" in text.upper() or "PLAY" in text.upper() or "START" in text.upper()) and ("MUSIC" in text.upper() or "SONG" in text.upper() or "SONGS" in text.upper()) :
        play_music()
        count+=1

    elif ("OPEN" in text.upper() or"START" in text.upper()) and ("MYSQL" in text.upper() or "SQL" in text.upper()) :
        open_sql()
        count+=1

    elif "MS" in text.upper() or "MICROSOFT" in text.upper() :
        ms(text)
        count+=1

    elif "WHO" in text.upper() or "HOW" in text.upper() or "WHAT" in text.upper() or ("TELL" in text.upper() and "ABOUT YOU" in text.upper()) :
        questions(text)
        count+=1

    for word in text.split() :
        for x in operations :
            if word.upper()==x :
                count+=1
                r=operations[x](l)
                print("ECHO : Result is = ",r)
                break

        if count==1 :
            break

        for x in commands :
             if word.upper()==x :
                count+=1
                commands[x]()
                break
        
        if count==1 :
            break

    if count==0 :
        sorry()

    print()
    input("Press Enter to Continue...\n")
