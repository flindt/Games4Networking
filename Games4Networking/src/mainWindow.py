'''
Created on Jan 12, 2012

@author: pfl
'''

'''
You all need to add a button to this main window. Put your game in a separate package.

remember to commit often !

Push your changes to your own repository on gitHub : "Team/Push upstream"
When you have something you want to share with the rest of us, make a "Pull request" on gitHub.

If you want the latest from some elses repository (maybe mine) you must do this:
    1 - add my repsotitory as an upstream fetch
            "Team / Remote / Configure Fetch from Upstream..."
    2 - get the code from this upstream repository
            "
'''
import tkinter as tk
 
def popout():
    def currencyconv():
        print("what do you want to exchange")
        what = input()
        print("and how much")
        x = int(input())
        if what == "ron" or "lei":
            euro = x*0.23
            dkk = x*1.71
            return(x,what, "inseamna",euro,"euroi si",dkk,"coroane")
        if what == "euro":
            ron = x*4.3
            dkk = x*7.4
            return(x,what, "inseamna",ron,"ron si",dkk,"coroane")
        if what == "dkk":
            ron = x*6
            euro = x*0.13
            return(x,what, "inseamna",ron,"ron si",euro,"euro") 
    other = tk.Toplevel()
    other.title("Victors Window")
    otherlabel = tk.Label(other, text='this is it', relief = tk.RIDGE)
    otherlabel.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)
    otherbutton = tk.Button(other, text='CLICK ME').pack(side=tk.TOP)
    otherbutton = tk.Button(other, text='NO,NO, CLICK ME').pack(side=tk.BOTTOM)
    

if __name__ == '__main__':
   
    
    win = tk.Frame()
    win.pack()
    
    # Flindt
    # Everyone should add their own button like this 
    
    buttonGameFlindt = tk.Button( win, text = "a puzzle", command = win.quit).pack(side=tk.TOP)
    buttonVictor = tk.Button( win, text="TEST", command=popout).pack(side=tk.BOTTOM)
    buttonQuit = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)    
    

#   labelVictor = tk.Label(win, text="Victors stuff here").pack(side=tk.BOTTOM)
#   e = tk.Entry(win)
#   e.pack(side=tk.BOTTOM)
#    def int2hex():
#        hex(int(e.get()))[2:]

    
    win.mainloop()
    
