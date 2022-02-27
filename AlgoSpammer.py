import sys,os
import pyautogui as pg
from time import sleep

def start_art(additional):
    art= """
    +-+-+-+-+-+-+-+-+-+-+-+
    |A|l|g|o|S|p|a|m|m|e|r|
    +-+-+-+-+-+-+-+-+-+-+-+
    """
    print(art+"\n"+ additional)

try:
    input_word = sys.argv[1] 
    if input_word =="-uf" or input_word=="-usefile":
        try:
            
            filename = sys.argv[2]
            
            try:
                spam_count =sys.argv[3]
                printtext="using the custom text file "+str(filename)+" "+str(spam_count)+" times to spam in 5 secs...\n press CTRL+C to terminate.\n"
                start_art(printtext)
                
                if os.path.isfile(filename):
                    sleep(5)
                    
                    for cnt in range(int(spam_count)):
                        custom_file = open(filename,"r")
                        for line in custom_file:
                            pg.typewrite(line)
                            pg.press("enter")
                        custom_file.close()
                    print("spamming through file done...")
                else:
                    sleep(0.5)
                    print("file doesn't exit, exiting spammer...")
                    exit()

            except IndexError:
                printtext="using the custom text file "+filename+" only once to spam in 5 secs...\n press CTRL+C to terminate.\n"
                start_art(printtext)
                
                if os.path.isfile(filename):
                    sleep(5)
                    custom_file = open(filename,"r")
                    for line in custom_file:
                        pg.typewrite(line)
                        pg.press("enter")
                    custom_file.close()
                    print("spamming through file done...")
                else:
                    sleep(0.5)
                    print("file doesn't exit, exiting spammer...")
                    exit()
        except IndexError:
            filename2= "spamtext.txt"
            try:
                spam_count =sys.argv[2]
                
                printtext="using default spamtext file "+str(spam_count)+" times in 5 secs...\n press CTRL+C to terminate.\n"
                start_art(printtext)
                sleep(5)
                for cnt in range(int(spam_count)):
                    f= open(filename2,"r")
                    for line in f:
                        pg.typewrite(line)
                        pg.press("enter")
                    f.close()
                print("spamming through file done, exiting spammer...")
            except IndexError:
                printtext="using default spamtext file only once in 5 secs...\n press CTRL+C to terminate.\n"
                start_art(printtext)
                sleep(5)
                f= open(filename2,"r")
                for line in f:
                    pg.typewrite(line)
                    pg.press("enter")
                f.close()
                print("spamming through file done, exiting spammer...")
    else:
        try:
            count = sys.argv[2]
            
            printtext="starting spamming \'"+input_word+"\' "+str(count)+" times"+" in 5 secs...\n press CTRL+C to terminate.\n"
            start_art(printtext)
            sleep(5)
            for cnt in range(int(count)):
                pg.typewrite(input_word)
                pg.press("enter")      
            print("\n spamming done, exiting spammer...")
             

        except IndexError:
            
            printtext="starting spam \'"+input_word+"\' in 5 secs...\n press CTRL+C to terminate.\n"
            start_art(printtext)
            sleep(5)
            while True:
                pg.typewrite(input_word)
                pg.press("enter")       

except IndexError:
    counter =0
    printtext="starting autoclick enter in 5 secs...\n press CTRL+C to terminate.\n"
    start_art(printtext)
    sleep(5)
    #if no args
    while True:
        counter +=1
        print(counter)
        pg.press("enter")
