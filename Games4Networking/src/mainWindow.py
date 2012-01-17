'''
Created on Jan 12, 2012

@author: pfl
'''

'''
You all need to add a button to this main window. Pushing your 
'''

if __name__ == '__main__':
    import tkinter as tk
    
    win = tk.Frame()
    win.pack()
    
    # Flindt
    buttonGameFlindt = tk.Button( win, text = "a puzzle", command = win.quit).pack(side=tk.TOP)
    
    buttonQuit = tk.Button( win, text = "Quit", command = win.quit).pack(side=tk.RIGHT)    
    
    win.mainloop()