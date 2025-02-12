# Modules
import os #Funky console clearing stuff
import random #RNG
import datetime #"[Name] has gone missing."
import time #Suspense/To look nice

#Functions
def clearscreen(): #Clears output console
    os.system('cls' if os.name == 'nt' else 'clear')
def strike(text): #Strikethrough
    i = 0
    new_text = ''
    while i < len(text):
        new_text = new_text + (text[i] + u'\u0336')
        i = i + 1
    return(new_text)
def buy(item): #Buy thing from shop
    int(item)
    clearscreen()
    wound=r"""⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢿⣷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣷⡙⠻⣿⣦⣄⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⣀⣤⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣆⠈⠻⠟⢻⣿⣿⣁⣀⣀⣠⣤⣶⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⣋⣤⣄⠀⠙⢿⣿⣿⡿⠿⣻⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠛⠋⠉⠛⢻⣿⣧⠀⠀⠉⠁⠀⣴⣿⣿⠀⠀⠀⢀⣀⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡿⠀⠀⠀⠀⠀⠸⣿⣿⣶⣶⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣯⣶⣾⣿⣿⣦⡀⠀⠈⠛⠛⣽⣿⡏⠀⠀⢀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠾⠟⠛⠉⠉⠀⠀⠀⢹⣿⣷⠀⠀⠀⠀⠻⣿⣧⣤⣴⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣫⣴⣶⣤⡀⠀⠙⠿⠟⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠿⠿⠿⢿⣿⣿⣆⠀⠀⠸⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠋⠁⠀⠀⠀⠀⠀⠹⣿⣧⣶⣶⣤⡈⢿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠟⠛⠉⠉⠙⠻⣶⣽⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢷⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀"""
    print(wound)
    time.sleep(1)
    print("A stinging pain enters your chest...")
    time.sleep(1)
    print("However...")
    time.sleep(3)
    clearscreen()
    if item==1:
        print("You obtained [BEATING HEART]")
        time.sleep(0.5)
        itemart=r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣶⣧⣰⣿⣿⠇⣼⣿⢻⣶⢴⠶⢦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⠟⢙⣿⣿⢣⢹⣿⡆⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡿⠙⢹⠗⣪⣿⣧⣾⣧⣾⣿⣧⠈⠻⣄⠀⠀⠀⠀⢀⣀⡀⠀
⠀⠀⠀⠀⠀⠀⢰⣇⢰⢏⠎⡴⣻⡿⠟⠉⠙⠋⣑⣆⠀⠈⠙⡶⠖⢺⣏⣽⣿⡆
⠀⠀⠀⠀⠀⠀⣿⣥⡏⢨⢸⣿⣿⡁⠀⠀⣤⣾⣿⣿⣿⣶⣦⣷⢶⣾⡿⠟⠛⠁
⠀⠀⠀⠀⠀⢸⣿⡟⢿⠯⣸⣿⡿⠠⠂⣾⡿⠟⠋⠁⠀⠀⠀⠉⠉⠉⠉⢹⣷⡀
⠀⠀⠀⠀⠀⢸⣿⣷⣰⣄⣿⣿⡗⠀⣤⣿⠃⠀⡀⣠⣖⣉⣵⡦⢀⣀⠀⢸⣏⡇
⠀⠀⢀⣴⠋⠉⠉⠩⠿⣿⡿⣿⣿⣿⡿⠃⡠⠞⣱⣿⣿⠟⠛⠻⣿⣿⣷⣾⣷⣷
⠀⠀⡼⣧⠆⠀⠀⠀⠀⣸⣿⣿⡟⠉⢀⣞⡴⢎⣿⣿⠓⠊⡹⣃⢙⣿⣿⣿⣛⠛
⠀⣼⣃⣯⠖⠁⢀⣤⣴⣿⡿⢏⡦⠊⠉⣿⣴⣿⢻⡈⣠⣧⢃⢣⣿⣧⢻⣿⣿⠃
⢸⣳⣏⣸⣿⣾⣿⣿⣿⣯⡀⢾⡁⠀⠀⠈⠉⠛⡿⣿⣯⣨⡷⢼⡿⠻⣿⠆⠉⠀
⢸⣾⢠⣿⣽⣾⣿⡥⠿⣿⣋⠓⠋⠦⠀⢀⢸⠀⣱⣿⣿⣿⡳⣾⣤⣀⣿⠀⠀⠀
⠸⣿⣷⣿⣿⣿⣿⣦⣤⣀⠘⢧⠤⠴⠞⣻⡶⢾⣿⣿⣿⠲⡏⢻⣿⣿⣿⠀⠀⠀
⠀⢻⣭⣿⣿⣿⡿⣿⣿⣽⡢⠄⡀⠀⢘⡟⢠⣿⡹⣿⣿⠀⠳⢸⢸⢹⡏⠀⠀⠀
⠀⠈⢻⣿⣸⣿⠯⠿⠿⡦⣻⡢⣄⠖⡩⠔⣿⣯⣿⢿⣟⠳⠄⡜⣻⣿⡇⠀⠀⠀
⠀⠀⢿⣿⣿⣿⠀⠀⠐⢸⢿⣷⡈⢁⡤⣾⣿⣿⡿⣿⣿⢷⣄⣁⠇⣿⡇⠀⠀⠀
⠀⠀⠘⣿⣿⣿⣷⣷⣀⢸⠻⣦⣁⡞⣰⣿⣿⣿⣹⣟⢹⣦⠘⠟⣴⣿⠇⠀⠀⠀
⠀⠀⠀⠹⣿⡿⣿⣍⢿⡟⢆⠉⠚⣰⣿⣿⣷⡸⡏⣿⡀⢷⣧⣰⢃⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣷⣌⢻⡳⡿⣾⣤⡞⢹⣿⠇⣸⡇⣹⡏⠀⢘⣷⣿⡾⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣄⣀⣹⢧⣿⣿⡆⠼⢡⢿⡇⠀⡿⣹⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣟⡦⣟⣻⣿⡡⣿⡆⣾⠸⣳⢀⣧⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣶⣿⣧⣹⢯⣷⣣⡼⣵⣻⣲⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣹⣽⡞⡃⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣛⡛⠛⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
        print(itemart)
        time.sleep(2)
        print("This can be used to bait creatures.")
        time.sleep(7.5)
    elif item==2:
        print("You obtained [MEAT HOOK]")
        time.sleep(0.5)
        itemart=r"""⠀⢤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢿⣦⡈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠰⣄⡉⢁⣤⡈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠳⣄⠙⢿⣦⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠰⣄⠙⢀⣤⡈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄⠙⢿⣦⡀⠰⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠙⢿⣦⡈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣄⠙⣡⣾⣷⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠋⠉⠉⠉⠛⠛⠿⣿⣶⣦⣤⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣷⠆⠀⠀⠀⣠⣾⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣶⣶⣿⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
        print(itemart)
        time.sleep(2)
        print("This can be used to fend off hostile creatures..")
        time.sleep(7.5)
    else:
        print("You obtained [FLESH MASS]")
        time.sleep(0.5)
        itemart=r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣀⣀⣀⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣯⣭⣽⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣽⣿⣿⣿⣿⣟⣿⣿⣿⣿⣟⢿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠉⠻⣿⣿⣿⣿⣿⣿⣟⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠘⣿⣷⢻⣿⣿⣿⡽⣿⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡏⣿⣿⣿⣿⣿⡟⠀⢀⣀⡀⠀⠘⣿⡟⣿⣿⣼⣿⣻⣛⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡿⢠⣶⣿⣿⣿⣿⡄⢹⣿⣿⣿⣿⣿⣿⣷⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣻⣿⣿⣿⣿⣿⣿⡇⣻⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣾⣿⣿⡇⠹⣿⣿⣿⣿⣿⡏⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠙⠛⠋⠁⠀⣾⣿⣿⣿⢫⣿⣿⣿⢹⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣽⣿⣿⣿⣿⣷⡀⠀⢀⣾⣿⣿⣿⣿⣿⣷⣯⣿⣿⣎⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣷⣤⣿⣿⣿⣿⣿⣿⣿⣿⡧⣿⢻⣾⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣏⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣁⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣧⣿⣟⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡿⠏⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠻⣿⣾⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣻⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠁⠀⠀⠀
"""
        print(itemart) #Yes the flesh mass is just something from omori shut up
        time.sleep(2)
        print("This will protect you from hostile creatures.")
        time.sleep(7.5)
def intro(): #Takes name and consent
    print("Hello.")
    time.sleep(1)
    print("What is your name?")
    time.sleep(1)
    name=input(">").capitalize()
    name=name.strip()
    print(str(name)+". What a lovely name.")
    time.sleep(2)
    print("This game will use a Y/N system, as well as typing numbers.")
    while True:
        time.sleep(2)
        print("Would you like to play?")
        time.sleep(1)
        consent=input(">")
        if consent.casefold()=="y":
            print("Great. I'll keep in touch.")
            time.sleep(3)
            return name
        elif consent.casefold()=="n":
            print("Oh?")
            time.sleep(1)
            print("Well, OK. Have a good day, "+name+".")
            time.sleep(1)
            exit()
        else:
            print("Remember, Y/N system.")
def gameover(howmany,where): #When you die
    clearscreen()
    time.sleep(5)
    print("...Silence.")
    time.sleep(3)
    print(name+" has gone missing.")
    time.sleep(1)
    print(f"They've been missing since {today:%B %d, %Y}.")
    time.sleep(5)
    clearscreen()
    time.sleep(1)
    print(".")
    time.sleep(1)
    clearscreen()
    print("..")
    time.sleep(1)
    clearscreen()
    print("...")
    time.sleep(3)
    print()
    print("A ringing of a phone is heard...")
    time.sleep(2.5)
    print()
    print("Error code: "+str(howmany))
    time.sleep(.5)
    print()
    exit("Please dial "+str(where)+" with the error code.")
def menu(): #Actual intro
    menu_art1=r'''                           (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\        ______    \    /   /\/\  /\/\
          /  \    //_\       \    /\    \  /\/\/    \/    \
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \
 /\/\/\/       //_______\       \|__|      \
/      \      /XXXXXXXXXX\                  \
        \    /_I_II  I__I_\__________________\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~
            
        _   _                ___  ___                    
       | | | |               |  \/  |                    
       | |_| | _____      __ | .  . | __ _ _ __  _   _   
       |  _  |/ _ \ \ /\ / / | |\/| |/ _` | '_ \| | | |  
       | | | | (_) \ V  V /  | |  | | (_| | | | | |_| |_ 
       \_| |_/\___/ \_/\_/   \_|  |_/\__,_|_| |_|\__, ( )
               _    _ _                  ___      __/ |/ 
              | |  | | |                |__ \    |___/ 
              | |  | | |__   ___ _ __ ___  ) |
              | |/\| | '_ \ / _ \ '__/ _ \/ / 
              \  /\  / | | |  __/ | |  __/_|  
               \/  \/|_| |_|\___|_|  \___(_)  
    '''
    menu_art2=r'''                          (   )
                           (    )
                          (    )
                           (    )
                           )  )
                            )  )                 /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\        ______    \    /   /\/\  /\/\
          /  \    //_\       \    /\    \  /\/\/    \/    \
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \
 /\/\/\/       //_______\       \|__|      \
/      \      /XXXXXXXXXX\                  \
        \    /_I_II  I__I_\__________________\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~
            
        _   _                ___  ___                    
       | | | |               |  \/  |                    
       | |_| | _____      __ | .  . | __ _ _ __  _   _   
       |  _  |/ _ \ \ /\ / / | |\/| |/ _` | '_ \| | | |  
       | | | | (_) \ V  V /  | |  | | (_| | | | | |_| |_ 
       \_| |_/\___/ \_/\_/   \_|  |_/\__,_|_| |_|\__, ( )
               _    _ _                  ___      __/ |/ 
              | |  | | |                |__ \    |___/ 
              | |  | | |__   ___ _ __ ___  ) |
              | |/\| | '_ \ / _ \ '__/ _ \/ / 
              \  /\  / | | |  __/ | |  __/_|  
               \/  \/|_| |_|\___|_|  \___(_)  
    '''
    for i in range(8):
        if i%2==0:
            clearscreen()
            print(menu_art1)
            time.sleep(1)
        else:
            clearscreen()
            print(menu_art2)
            time.sleep(1)
    clearscreen()
    print(".")
    time.sleep(2)
    clearscreen()
    print("..")
    time.sleep(3)
    clearscreen()
    print("...")
    time.sleep(2)
    clearscreen()
    print("....")
    time.sleep(0.5)
    clearscreen()
    print("....Where am I?")
    time.sleep(3)
    while True:
        print("Get up?")
        awake=input(">")
        if str.strip(awake)=="y" or str.strip(awake)=="Y":
            print("You get up from the cold ground...")
            time.sleep(2)
            break
        elif str.strip(awake)=="n" or str.strip(awake)=="N":
            print("I'm sure there's nothing to worry about...")
            time.sleep(3)
            print()
            print("...Right?")
            time.sleep(5)
            gameover(1122121,9253087)
        else:
            print("...What?")
            time.sleep(1)
def startroom(first,crowbar): #A tutorial of sorts
    clearscreen()
    if first==True:
        print("You were on the ground of a tiled room with concrete walls.")
        time.sleep(2)
        print("There is an open closet on the other side of the room.")
        time.sleep(2)
        print("A small dresser with a antique phone is under a window.")
        time.sleep(2)
        print("There is a table behind you. Maybe you fell off of it?")
        time.sleep(2)
        print("There is a door on the right wall.")
        time.sleep(2)
    else:
        print("The empty room is comforting.")
        time.sleep(2)
    print("What should you do?")
    time.sleep(2)
    print(" 1. Leave room through door.")
    time.sleep(1)
    print(" 2. Investigate dresser.")
    time.sleep(1)
    print(" 3. Go in closet.")
    time.sleep(1)
    while True:
        decision=input(">")
        if decision=="1":
            if crowbar==True:
                print("You pryed open the door with the crowbar you found and go through.")
                time.sleep(1)
                print("Barely, though. The crowbar breaks in use.")
                time.sleep(3)
                livingroom(True,str(blood),False,False,False)
            else:
                print("It's locked from the outside. I need a tool to open it.")
                time.sleep(3)
                startroom(False,False)
        elif decision=="2":
            print("The phone on the dresser has a small note next to it.")
            time.sleep(1)
            print("Read it?")
            decision=input(">")
            if decision=="y".casefold():
                print("'Dear "+name+",'")
                time.sleep(3)
                print("'How many times is first,")
                time.sleep(1)
                print("'What to press is last.'")
                time.sleep(1)
                print("What could that mean..?")
                time.sleep(7.5)
                startroom(False,crowbar)
            elif decision=="n".casefold():
                startroom(False,crowbar)
            else:
                print("...I'll take that as a no.")
        elif decision=="3":
            print("You take a step into the dark, open closet...")
            time.sleep(3)
            clearscreen()
            time.sleep(1)
            print("˙˙˙ʇɥƃᴉɹ lǝǝɟ ʇ,usǝop ʇǝsolɔ ʞɹɐp sᴉɥ┴")
            time.sleep(3)
            print("¿ʇɐɥʇ s,ʇɐɥʍ 'ʇᴉɐM")
            time.sleep(2)
            if crowbar==False:
                print("You obtained [CROWBAR]")
                time.sleep(0.5)
                crowbar=True
                crowbart=r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣶⡄⠱⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⡙⣿⣿⡄⢹⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡿⢋⣠⠾⠋⠉⢹⣿⣷⢸⣿⡆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⠏⣠⠞⠁⠀⠀⠀⢸⣿⣿⢸⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⢡⡾⠋⠀⠀⠀⠀⠀⢸⣿⡇⢸⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠁⣴⡟⠁⠀⠀⠀⠀⠀⠀⣿⡿⠀⣾⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⣼⠟⢁⣼⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣄⠁⠰⡿⠃⠀⠀⠀⠀⠀⠀⢠⡾⠁⣴⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⢀⡿⢀⣾⣿⣿⣿⡇⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⣼⡿⢃⣿⣿⠇⠀⠀⠀
⠀⠀⠀⢠⣾⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣼⠟⠁⣸⣿⠏⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠃⠀⠀⠀⠀⠀
⠀⣾⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
                print(crowbart)
                time.sleep(5)
                print("˙˙˙lnɟǝsn ǝq ll,sᴉɥ┴")
                time.sleep(3)
                print("˙ɥƃnoɥʇ ʇǝsolɔ sᴉɥʇ ɟo ʇno ʇǝƃ oʇ pǝǝu I˙˙˙")
                time.sleep(5)
                startroom(False,True)
            else:
                time.sleep(1)
                print("˙ɹǝƃuol ɥɔnɯ ǝɹǝɥ uᴉ ʎɐʇs plnoɥs I ʞuᴉɥʇ ʇ,uop I˙˙˙")
                time.sleep(3)
                print("¿ʇǝsolɔ ǝɥʇ ǝʌɐǝl I plnoɥS")
                time.sleep(1)
                decision=input("<")
                if decision=="n".casefold():
                    print("˙˙˙ǝɹǝɥʇ s,ʇɐɥʍ ʇno ǝʞɐɯ oʇ ƃuᴉʎɹʇ ʇǝsolɔ ǝɥʇ uᴉ ʎɐʇs ǝM")
                    time.sleep(2)
                    print("˙˙˙ʇᴉɐM")
                    time.sleep(5)
                    print("˙˙˙˙˙ou ɥO ˙˙ɥO")
                    time.sleep(1)
                    gameover(12113211, 43806818)
                elif decision=="y".casefold():
                    print("˙ʇǝsolɔ ǝƃuɐɹʇs ǝɥʇ ǝʌɐǝl ǝM")
                    time.sleep(3)
                    startroom(False,crowbar)
                else:
                    print("¿ʞuᴉɥʇ oʇ ǝɯᴉʇ ǝɹǝɥʇ sI")
                    time.sleep(1)
                    print("˙˙˙ʇᴉɐM")
                    time.sleep(3)
                    print("˙˙˙˙˙ʇ,usᴉ ǝɹǝɥ┴ ˙˙˙oN")
                    time.sleep(0.5)
                    gameover(12113211, 43806818)
        else:
            print("Not sure what that means.")
def livingroom(first,blood,heart,hook,mass,attempted): #Main room !UNFININISHED!
    clearscreen()
    int(blood)
    if first==True:
        print("You enter a large, warmly lit living room.")
        time.sleep(2)
        print("There is a nice fireplace with an ongoing fire in it.")
        time.sleep(2)
        print("In front of the fireplace is a nice couch.")
        time.sleep(2)
        print("There seems to be... something on the couch.")
        time.sleep(2)
        print("The living room is connected to multiple rooms.")
        time.sleep(2)
        print("A kitchen, a bathroom, a guest room, they have it all.")
        time.sleep(2)
    print("The warm fire and 'friend' is nice to have.")
    time.sleep(2)
    print("What should you do?")
    time.sleep(1)
    print(" 1. Talk with the... thing.")
    time.sleep(1)
    print(" 2. Check the kitchen.")
    time.sleep(1)
    print(" 3. Check the bathroom.")
    time.sleep(1)
    print(" 4. Check the guest room.")
    time.sleep(1)
    print(" 5. Stay by the fireplace.")
    time.sleep(1)
    if attempted:
        print(" 6. Go back into the original room.")
    else:
        print(strike(" 6. Go back into the original room"))
        print("    Attempt to go back into original room.")
    time.sleep(1)
    while True:
        decision=input(">")
        if decision=="1": #Shop/'Friend'
            print("You approach the creature on the couch.")
            time.sleep(2)
            clearscreen()
            friend=r"""                            ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \
            /   /     ||--+--|--+-/-|     \   \
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
             
            """
            print(friend)
            time.sleep(1)
            print("'Well hello, fresh meat.'")
            time.sleep(3)
            print("'I am willing to give you helpful items,")
            print("in exchange for your blood.'")
            time.sleep(3)
            print("'You only have so much though, and I'm not")
            print("the only one who wants it.'")
            time.sleep(2)
            print("'Spend wisely.'")
            time.sleep(3)
            clearscreen()
            print(friend)
            while True:
                clearscreen()
                print(friend)
                print("Press N to leave shop any time.")
                print("Your current blood level is "+str(blood)+".")
                time.sleep(2)
                print()
                print("1. Beating Heart - 10 blood")
                print("   'Can be used as bait.'")
                print("2. Meat hook - 25 blood")
                print("   'Can be used to deter pests.'")
                print("3. Flesh Mass - 75 blood")
                print("   'Deters pests easier and doesn't break.'")
                item=input(">").strip()
                if item=="1" or item=="2" or item=="3":
                    print("Are you sure?")
                    time.sleep(1)
                    while True:
                        decision=input(">")
                        if decision=="n".casefold():
                            break
                        elif decision=="y".casefold():
                            if item=="1":
                                if heart==True:
                                    print("'You already have a beating heart.'")
                                    time.sleep(3)
                                    break
                                else:
                                    if int(blood)>10:
                                        print("'I'll take your blood for it then.'")
                                        time.sleep(3)
                                        buy(1)
                                        blood=int(blood)-10
                                        heart=True
                                        break
                                    else:
                                        print("'You don't have enough blood. I don't want to kill you quite yet.'")
                                        time.sleep(3)
                                        break
                            elif item=="2":
                                if hook==True:
                                    print("'You already have a meat hook.'")
                                    time.sleep(3)
                                    break
                                else:
                                    if int(blood)>25:
                                        print("'I'll take your blood for it then.'")
                                        time.sleep(3)
                                        buy(2)
                                        blood=int(blood)-25
                                        hook=True
                                        break
                                    else:
                                        print("'You don't have enough blood. I don't want to kill you quite yet.'")
                                        time.sleep(3)
                                        break
                            elif item=="3":
                                if mass==True:
                                    print("'You already have a flesh mass.'")
                                    time.sleep(3)
                                    break
                                else:
                                    if int(blood)>75:
                                        print("'I'll take your blood for it then.'")
                                        time.sleep(3)
                                        buy(3)
                                        blood=int(blood)-75
                                        mass=True
                                        break
                                    else:
                                        print("'You don't have enough blood. I don't want to kill you quite yet.'")
                                        time.sleep(3)
                                        break
                elif item=="n".casefold():
                    print("'Fairwell, friend. I will be here until the end of time.'")
                    time.sleep(3)
                    livingroom(False,blood,heart,hook,mass)
                else:
                    print("'I don't have that. Pick something I have.'")
                    time.sleep(3)
        elif decision==2:
            print("Haiiii")
            livingroom(False,blood,heart,hook,mass)
        elif decision=="4":
            print("Haiiii")
            livingroom(False,blood,heart,hook,mass)
        elif decision=="5":
            print("Haiiii")
            livingroom(False,blood,heart,hook,mass)
        elif decision=="6": #Notice you can't go back
            clearscreen()
            print("You try to enter the room again, but the door seemingly repaired.")
            time.sleep(1)
            door=r"""
.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..
   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  
      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  
..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..
   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    
   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     
   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     
___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____
      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  
      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  
      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  
     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  
..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..
   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     
   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     
  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  
-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-
      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  
     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  
  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  
"""
            print(door)
            time.sleep(5)
            livingroom(False,str(blood),heart,hook,mass,True)
        else: #Failsafe
            print("Not sure what that means.")

# Everything below here is where the actual game is
clearscreen()
name=intro()
today=datetime.date.today()
menu()
heart=False
hook=False
mass=False
crowbar=False
blood=100
startroom(True,False)
if blood<1:
    gameover(221211131132,531370872125)