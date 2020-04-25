# from tkinter import *
import time
from pynput import keyboard, mouse
while True:
    def clicker(x, y):
        tim1 = time.time()
        print('Working...')
        time.sleep(2)
        mouse.Controller().position = (x, y)
        m = mouse.Controller()
        m.click(mouse.Button.left, 2)
        tim2 = time.time()
        print('Clicking is don. in ' + str((int(tim2) - int(tim1))))
        time.sleep(0.5)
        print('Going to type words...')


    def typer(words, from_filee, way):
        tim1 = time.time()
        if from_filee == 0:
            print('connected to typing program...')
            time.sleep(0.5)
            print('Working...')
            time.sleep(2)
            z = words.strip("")
            kb = keyboard.Controller()
            for i in range(0, len(z)):
                if z[i] == " ":
                    kb.press(keyboard.Key.space)
                # elif z[i]==" ":
                elif z[i] == "\n":
                    kb.press(keyboard.Key.enter)
                else:
                    kb.press(z[i])
            tim2 = time.time()
            print('typing is don.'+str((int(tim2) - int(tim1))))
            print('program is end.')

        elif from_filee == 1:
            print('connected to typing program...')
            time.sleep(0.5)
            print('Working...')
            time.sleep(2)
            f = open(way, 'r')
            y12 = f.readlines()
            f.close()
            # z0=y12.
            # z = words.strip("")
            kb = keyboard.Controller()
            for i in range(0, len(y12)):
                z = y12[i].strip("")
                for i2 in range(0, len(z)):
                    if z[i2] == " ":
                        kb.press(keyboard.Key.space)
                    # elif z[i]==" ":
                    elif z[i2] == "\n":
                        kb.press(keyboard.Key.enter)
                    else:
                        kb.press(z[i2])
            tim2 = time.time()
            print('typing is don.in ' + str((int(tim2) - int(tim1))))



    from_filee = 0
    x = input("Enter x of mouse area clicker : ")
    y = input("Enter y of mouse area clicker : ")
    words = input(
        "Enter the words what you like to typing. Or enter(from_file) if you whant tou type it from a file : ")
    if words == "from_file":
        from_filee = 1
        way = input('Enter File Way : ')
        clicker(int(x), int(y))
        typer(words, from_filee, way)
    else:
        way = 0
        clicker(int(x), int(y))
        typer(words, from_filee, way)
    cent=input('Do you whant to continue?y/n : ')
    if cent=="n":
        break
