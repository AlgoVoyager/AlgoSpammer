import sys,os
import pyautogui as pg
from time import sleep
counter =0
try:
    input_word = sys.argv[1]
    if input_word =="-uf" or input_word=="-usefile":
        try:
            filename = sys.argv[2]
            print("using the custom text file "+filename+" to spam in 5 secs...\n press CTRL+C to terminate.")
            sleep(5)
            if os.path.isfile(filename):
                custom_file = open(filename,"r")
                for line in custom_file:
                    pg.typewrite(line)
                    pg.press("enter")
                custom_file.close()
                print("spamming through file done...")
            else:
                print("file doesn't exit, exiting spammer...")
                exit()
        except IndexError:
            filename= "spamtext.txt"
            print("\n using default spamtext file in 5 secs...\n press CTRL+C to terminate.")
            sleep(5)
            f= open(filename,"r")
            for line in f:
                pg.typewrite(line)
                pg.press("enter")
            f.close()
            print("spamming through file done...")
    else:
        try:
            count = sys.argv[2]
            print("\n starting spamming \'"+input_word+"\' "+str(count)+" times"+" in 5 secs...\n press CTRL+C to terminate.")
            sleep(5)
            for cnt in range(int(count)):
                pg.typewrite(input_word)
                pg.press("enter")      
             

        except IndexError:
            print("\n starting spamming \'"+input_word+"\' in 5 secs...\n press CTRL+C to terminate.")
            sleep(5)
            while True:
                pg.typewrite(input_word)
                pg.press("enter")       

except IndexError:
    print("starting autoclick enter in 5 secs...\n press CTRL+C to terminate.")
    sleep(5)
    #if no args
    while True:
        counter +=1
        print(counter)
        pg.press("enter")
