if __name__ == '__main__':
    import tkinter as tk
    import time
    
    win = tk.Frame()
    win.pack()
    
    # Flindt
    # Everyone should add their own button like this 
    buttonGameFlindt = tk.Button( win, text = "a puzzle", command = win.quit).pack(side=tk.TOP)
    
    buttonGameNilsas = tk.Button( win, text = "The game", command = win.quit).pack(side=tk.TOP)
    
    buttonQuit = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.TOP)    
    
    win.mainloop()
    
    global gold
    global apples
    gold = 0
    apples = 0
    
    def start():
        print("Hello and welcome!")
        name = input("What's your name?")
        print ("Welcome, "+name)
        print ("The objective of this game is to collect apples")
        print ("After you collect all the apples, you sell them")
        choise = input ("Do you want to play? Y/N")
        if choise == "Y" :
            begin()
        if choise == "N" :
            print("Okay, bye then... ", command = win.quit)
            
    def begin():
        global apples
        global gold
        print("Let's get started then!")
        if gold > 99 :
            print ("Congratulations you have Won the Game!!")
            play = input("Do you want to play again? Y/N")
            if play == "Y" :
                begin()
            if play == "N" :
                print ("Congratz again!")
                time.sleep(2)   
                quit() 
        pick = input("Do you want to pick an apple? Y/N")
        if pick == "Y" :
            time.sleep(1)
            print("You just picked an apple.")
            apples=apples+1
            print("You now have, ",apples,"apples")
            begin()
        if pick == "N" :
            sell = input("Do you want to sell the apples? Y/N")
            if sell == "Y" :
                global gold
                global apples
                print("You currently have, ",apples,"apples")
                print("You have sold your apples.")
                gold=apples*10
                apples=0
                print("Your gold is now: ",gold)
                if gold > 99 :
                    begin()
                elif gold < 101 :
                    print ("So, are you done with this game?")
                    quiting = input("Do you give up? Y/N")
                    if quiting == "Y" :
                        print("Okay, see ya later.")
                        win.quit()
                    if quiting == "N" :
                        begin()
            if sell == "N" :
                print("Okay, see you later")
                quit()
    start()