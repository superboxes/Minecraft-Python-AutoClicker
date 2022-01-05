"""
Created by NEWE
Telegram : https://t.me/MondialMarketplace0
31/05/2021
"""
"""
GUI is made by SuperBoxes
Discord: bimbalas#9412
"""

import keyboard
import mouse
import time, random, threading
from colorama import init, Fore
from tkinter import *
from tkinter import messagebox

def autoclicker(k, c):
    while True:
        randomInt = float(random.uniform(0.01, 0.06))
        keyboard.wait(k)
        mouse.click('left')
        SSS = c + randomInt
        time.sleep(SSS)



def Submit(): ## Here goes the user after pressing the button!
    global key
    global delay
    error = False
    key = keyEntry.get()
    try:
        delay = float(delayEntry.get())
    except ValueError:
        messagebox.showwarning(title="Incorrect",
                               message="At the delay choice, enter a number (seconds)")
        messagebox.showinfo(title="Info", message="Now you have to turn off the program!")
        exit()
        error = True
    if not error:
        window.destroy()
        print("Autocliker key is: ",key,"")
        print("")
        print("")
        print("Turn off the cmd screen to turn off the AutoClicker")
        x = threading.Thread(target=autoclicker(key, delay), daemon=True)
        x.start
    else:
        exit()



init(convert=True)

window = Tk()
window.title("Autocliker by NEMU") ## window title
Label(window, text="AutoClicker", font=("Comic Sans MS", '20'), fg="green").grid(row=0, column=1)
label = Label(window, text="Key: ", font=("Arial", '20', "bold"))
label.grid(row=1, column=0)
keyEntry = Entry(window, font=("Arial", '20', "bold"))  ## place where you enter the key
keyEntry.grid(row=1, column=1)
label2 = Label(window, text="Delay (0 to 0.5): ", font=("Arial", '20', "bold"))
label2.grid(row=2, column=0)
delayEntry = Entry(window, font=("Arial", '20', "bold")) ## place where you enter the delay
delayEntry.grid(row=2, column=1)
button = Button(window, text="Start AutoClicker", font=("Arial", '15'), command=Submit).grid(row=4, column=1)
window.resizable(False, False)
window.mainloop()


