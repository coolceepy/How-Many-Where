import os #Ignore these
import time
def clearscreen(): #And this
    os.system('cls' if os.name == 'nt' else 'clear')

def name(first): #Replace 'name' with the room name.
    clearscreen()
    if first==True: #Change all these to match the room.
        print("Description 1")
        time.sleep(2)
        print("Description 2")
        time.sleep(2)
        print("Description 3")
        time.sleep(2)
        print("Description 4")
        time.sleep(2)
        print("Description 5") #Make as many as needed.
        time.sleep(2)
    else:
        print("Vague Description") #Give a vague (and ominous) description.
        time.sleep(2)
    print("What should you do?")
    time.sleep(2)
    print(" 1. This is an option.") #Change these option descriptions.
    time.sleep(1)
    print(" 2. This, too, is an option..")
    time.sleep(1)
    print(" 3. This is also an option..") #Make as many as needed.
    time.sleep(1)
    while True:
        decision=input(">")
        if decision==1:
            #What happens when this option is picked?
            print("Haiiii")
        elif decision==2:
            #Ditto
            print("Haiiii")
        elif decision==3:
            #Ditwo
            print("Haiiii")
        else:
            print("Not sure what that means.") #This stays the same except for special cases.
