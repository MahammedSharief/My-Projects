import datetime
from time import sleep
import re
import random
global a
def timeCheck(time):
    global tr
    if int(time[:2]) >= 6 and int(time[:2]) <= 12:
        tr = 0
        return "Good Morning!"
    elif int(time[:2])>12 and int(time[:2])<16:
        tr = 1
        return "Hey Good noon"
    elif int(time[:2])>=16 and int(time[:2])<19:
        tr = 2
        return "You chilling in this pleasant evening"
    else:
        tr = 3
        return "Hey it's too late! I shouldn't say GN right away ig :)"
def patience(x,time):
    sleep(time/10000)
    return x
def nameDecide():
    req_count = 0
    global user_name
    global weirdNames
    weirdNames = [r"no.*"]
    isWeird = False
    user_name = input("Btw can i know your sweet name \U0001F642 ")
    if re.search(weirdNames[0],user_name):
        print(f"What u mean by {user_name}")
        isWeird==True
    while (user_name.lower() == "no") or re.search(weirdNames[0],user_name):
        if req_count==0:
            print("Don't be too secretive about it. I've just asked your name \U0001F641")
            print("Now u will be a good person and tell me your name right?")
            print(patience("Don't say no",10000))
            user_name = input("Name pls : ")
        elif req_count==1:
            print("\U0001F620 you are too cruel ")
            print("maybe u good \U0001F97A")
            user_name = input()
        else:
            print("hey it's okay i'll refer to you as Default User")
            user_name = "Default User"
        req_count+=1
    a = input("I want to ask you something, Shall I? ")
    if "nope" in a.lower() or "no" in a.lower():
        print("Ok chill, Btw nice name")
    else:
        print("How can i address you")
        a = input("like bro, mate or not ")
        if "no" in a:
            return user_nam
        else:
            print("Okay",a)
            return a
def decideFood(tr):
    if tr == 0:
        return "breakfast"
    elif tr == 1:
        return "lunch"
    elif tr==2:
        return "snacks"
    else:
        return "dinner"
timeNow = datetime.datetime.now().time()
print(timeCheck(str(timeNow)))
nameDecide()
print("How u doing?",a)
while True:
    response = input()
    if "bad" in response.lower() or ("not" in response.lower() and "not" in re.split(response," ")):
        print("I’m sorry to hear that. Is there anything I can do to cheer you up?")
    elif "good" in response.lower() or "fine" in response.lower() or "good" in response.lower():
        print("That’s great to hear. What are you up to today?")
    elif "nothing" in response.lower() or "no" in response.lower():
        print("so u don't want anything from me")
        a =  input()
        if "yes" in a.lower() or "nothing" in a.lower():
            break
        else:
            print("So what's up?")
            continue
    elif "hungry" in response.lower():
        food = decideFood(tr)
        fres = input(f"Btw did u have {food} : ")
        if "yes"==fres:
            print("Cool")
        else:
            print("ohh go and have it now\nAnything else ")
        print("Quick reminder for u remember to STAY HYDRATED!")
    elif "tq" in response.lower() or "thank" in response.lower():
        break
    elif "joke" in response.lower():
        jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't some fish play piano? Because you can't tuna fish!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call fake spaghetti? An impasta!"
        ]
        jkWant = True
        jkCount = 1
        while jkWant:
            print(jokes[random.randint(0,len(jokes)-1)])
            jkCount+=1
            if jkCount>len(jokes):
                print("My jokes collection is over \U0001F605\U0001F605")
                break
            a = input("Do you want one more? ")
            if "yes" in a:
                print("You are enjoying ig here's one more")
                continue
            else:
                jkWant==False
                break
    else:
        print("Sorry, I am not able to understand what you said\nCan i help you with anything other than this")
        a =  input()
        if "no" in a.lower() or "nothing" in a.lower():
            break
    
if tr==3:
    print("It has been nice chatting with you, See you")
    print(patience("Btw Good Night",1000))
else:
    print("Ok bye:)")


    



