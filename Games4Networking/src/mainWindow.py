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
    other = tk.Toplevel()
    other.title("Second Window")
    otherlabel = tk.Label(other, text='this is it', relief = tk.RIDGE)
    otherlabel.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)
    

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
    
