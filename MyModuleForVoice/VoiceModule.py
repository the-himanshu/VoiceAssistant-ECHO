# Import all the required modules
import os
import pyttsx3
import wikipedia
import webbrowser
import random
def instruction() :                                     # Function to print instructions
    print("INSTRUCTION -: Please don't use any punctuation marks while communicating with me except for following a question with ?")

def listen() :                                          # Function to make ECHO listen
    import speech_recognition as sr
    ear=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        ear.pause_treshold=1
        audio=ear.listen(source)

    try :
        print("Recognizing...")
        string=ear.recognize_google(audio,language="en-in")
    except :
        string="Sorry Unable to recognize it please speak it again..."

    return string
    
def speak(text) :                                       # Function to make him talk
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-20)
    engine.say(text)
    engine.runAndWait()

def wiki(text) :                                       # Function to search something on wikipedia
    print("ECHO : ",end="")                                       
    print("Searching Wikipedia...")
    speak("Searching Wikipedia...")
    text=text.lower()
    text=text.replace("wikipedia","")
    text=text.replace("search","")
    text=text.replace("what is a","")
    try :
        result=wikipedia.summary(text,sentences=4)
        speak("According to wikipedia")
        print(result)
        speak(result)
    except :
        string="Sorry.. could not complete the search.. please try again"
        print(string)
        speak(string)

def open_youtube() :                                        # Function to open youtube
    print("ECHO : ",end="")                                    
    string="Opening Youtube..."
    print(string)
    speak(string)
    webbrowser.open_new_tab("youtube.com")

def open_google() :                                           # Function to open google
    import time
    print("ECHO : ",end="")                                    
    string="Opening Google..."
    print(string)
    speak(string)
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Google Chrome.lnk")
    time.sleep(2)

def open_sql() :                                                 # Function to open MySQL
    string="Opening MySQL..."
    print(string)
    speak(string)
    os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 5.5\\MySQL 5.5 Command Line Client.lnk")

def adobe(text) :                                                 # Function to open Adobe Applications
    if "READER" in text.upper() :
        print("ECHO : ",end="")
        string="Opening Adobe Reader..."
        print(string)
        speak(string)
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Reader XI.lnk")
        return
    if "PHOTOSHOP" in text.upper() :
        print("ECHO : ",end="")
        string="Opening Adobe Photoshop..."
        print(string)
        speak(string)
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\\Adobe Photoshop.lnk")
        return

def ms(text) :                                                     # Function to open Microsoft Applications
    import time
    if "POWERPOINT" in text.upper() or "POWER POINT" in text.upper() or "PP" in text.upper() :
        print("ECHO : ",end="")
        string="Opening Microsoft Powerpoint..."
        print(string)
        speak(string)
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk")
        return
    elif "WORD" in text.upper() :
        print("ECHO : ",end="")
        string="Opening Microsoft Word..."
        print(string)
        speak(string)
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Microsoft Office Word 2007.lnk")
        return
    elif "EXCEL" in text.upper() :
        print("ECHO : ",end="")
        string="Opening Microsoft Excel..."
        print(string)
        speak(string)
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Microsoft Office Excel 2007.lnk")
        return
    elif "PAINT" in text.upper() :
        print("ECHO : ",end="")
        string="Opening Microsoft Paint..."
        print(string)
        speak(string)
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\\Paint.lnk")
        time.sleep(1)
        return


def play_music() :                                                    # Function to play music
    print("ECHO : ",end="")
    string="Opening Music..."
    print(string)
    speak(string)
    music_directory="F:\My Programs\Python Projects\Voice Assistant AI\MusicForExample"
    songs=os.listdir("F:\My Programs\Python Projects\Voice Assistant AI\MusicForExample")
    number=1
    for song in songs :
        print(number,"->",end=" ")
        print(song)
        number+=1
    import random
    i=random.randint(0,number-1)
    while True :
        os.startfile(os.path.join(music_directory,songs[i]))
        x=int(input("\nEnter 1 -> Play New Song\nEnter 2 -> Play Next Song\nEnter 3 -> Play Previous Song\nEnter 4 -> Exit\n\nEnter your choice = "))
        if x==4 :
            return
        if x==1 :
            i=int(input("Enter the serial number of song = "))
            i=i-1
        if x==2 :
            if i==number-2 :
                i=0
            else :
                i=i+1
        if x==3 :
            if i==0 :
                i=number-2
            else :
                i=i-1

def extract_numbers(data) :                             # Function to extract numbers from the text
    li=[]
    for x in data.split(' ') :
        try :
            li.append(float(x))
        except :
            pass
    return li

def lcm(li) :                                           # Function to calculate LCM of 2 numbers
    a=li[0]
    b=li[1]
    l=a if a>b else b
    temp=l
    while l%a!=0 or l%b!=0 :
        l=l+temp
    return l

def hcf(li) :                                           # Function to calculate LCM of 2 numbers
    a=li[0]
    b=li[1]
    l=a if a>b else b
    temp=l
    while l%a!=0 or l%b!=0 :
        l=l+temp
    return (a*b)/l

def add(li) :                                           # Function to add n numbers
    sum=0
    for i in li :
        sum+=i
    return sum

def sub(li) :                                           # Function to find difference of two numbers
    return li[0]-li[1]

def mul(li) :                                           # Function to multiply n numbers
    pro=1
    for i in li :
        pro*=i
    return pro

def div(li) :                                           # Function to divide two numbers
    return li[0]/li[1]

def power(li) :                                         # Function to find power of one number raised to power another
    return li[0]**li[1]

def fact(li) :                                          # Function to calculate factorial of a number
    a=li[0]
    b=1
    while a>0 :
        b=b*a
        a-=1
    return b

def log(li) :                                           # Function to calculate natural log
    import math
    return math.log(li[0])

def time() :                                            # Function to print current time
    import time
    current_time=time.asctime(time.localtime(time.time()))
    z=current_time.split()
    print("Currrent Time is = ",z[3])

def date() :                                            # Function to print today date
    import time
    current_time=time.asctime(time.localtime(time.time()))
    z=current_time.split()
    print("Today Date is  =",end=" ")
    print(z[2],z[1],z[4],end=" ")
    print("and the day is",z[0])

def myName() :                                          # Function to print name of AI assistant
    string="My Name is Voice... I am your Virtual Assistant"
    print(string)
    speak(string)

def end() :                                             # Function to end program
    string="Thank you for using my service.. Kindly visit me again"
    print(string)
    speak(string)
    input("\nPress enter to exit")
    exit()

def hello() :                                            # Function to print hello
    string="Yes Sir.."
    print(string)
    speak(string)

def greet() :                                            # Function to print greetings
    import time
    current_time=time.asctime(time.localtime(time.time()))
    z=current_time.split()
    z=z[3].split(':')
    if z[0]>="0" and z[0]<"12" :
        string="Good Morning..."
    elif z[0]>="12" and z[0]<"17" :
        string="Good Afternoon..."
    else :
        string="Good Evening..."
    print("ECHO : ",end="")
    print(string)
    speak(string)

def questions(text) :                                      # Function to print answers to questions
    if ("MADE" in text.upper() or "CREATED" in text.upper()) and "YOU" in text.upper() :
        string="I was created by Himanshu Malik.."
    elif "HOW ARE YOU" in text.upper() and ("HEY" in text.upper() or "HELLO" in text.upper() or "" in text.upper())  :
        responses=["I am feeling great...","I am totally fine...","I am well!!","I am feeling awesome...","Just getting bored..","Feeling Amazing"]
        i=random.randint(0,5)
        string=responses[i]
    elif "ARE YOU DOING" in text.upper() :
        string="Nothing just waiting for your commands.."
    elif "WHAT IS YOUR AGE" in text.upper() :
        string="I am a Machine.. I don't have an age.. However i was developed in July 2019.."
    elif "ARE YOU" in text.upper() or ("TELL" in text.upper() and "ABOUT YOU" in text.upper()) :
        string1="I am ECHO.. I am your virtual assistant and was created by Himanshu Malik..\nI can help you in various Tasks such as "
        string2="Opening Web Applications, Opening Microsoft Applications, Playing Music and performing Mathematical Calculations...\n"
        string3="I am currently under development and more and more features will be added soon."
        string=string1+string2+string3
    else :
        string="SORRY!! i am unable to answer this question.."
    print("ECHO : ",end="")
    print(string)
    speak(string)

def help() :                                                 # Function to print help message
    print("ECHO : ",end="")
    string="How may i help you?"
    print(string)
    speak(string)

def sorry() :                                                 # Function to print sorry message
    print("ECHO : ",end="")
    string="Sorry.. but this problem is beyond my reach"
    print(string)
    speak(string)

operations={"ADD":add,"SUM":add,"ADDITION":add,"PLUS":add,"+":add,"DIFFERENCE":sub,"SUBTRACT":sub,"-":sub,"MINUS":sub,"MULTIPLY":mul,"PRODUCT":mul,"MULTIPLICATION":mul,
            "*":mul,"INTO":mul,"DIVIDE":div,"DIVISION":div,"POWER":power,"HCF":hcf,"LCM":lcm,"FACTORIAL":fact,"LOG":log,"LOGARITHM":log}

commands={"NAME":myName,"END":end,"EXIT":end,"HALT":end,"BYE":end,"ABORT":end,"BYE":end,"CLOSE":end,"HELP":help,"HELLO":hello,"HI":hello,"TIME":time,"DATE":date}
