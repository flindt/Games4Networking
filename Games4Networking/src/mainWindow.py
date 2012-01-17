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



if __name__ == '__main__':
    import tkinter as tk
    
    win = tk.Frame()
    win.pack()
    
    # Flindt
    # Everyone should add their own button like this 
    buttonGameFlindt = tk.Button( win, text = "a puzzle", command = win.quit).pack(side=tk.TOP)
    
    buttonQuit = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)    
    
    win.mainloop()