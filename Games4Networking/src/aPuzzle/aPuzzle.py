'''
Created on Jan 17, 2012

    This is a very simple puzzle 

@author: pfl
'''
import tkinter as tk



if __name__ == '__main__':
    puzzleWin = tk.Frame()
    puzzleWin.pack()
    
    buttonQuit = tk.Button( puzzleWin, text = "Quit", command = puzzleWin.quit).pack(side=tk.RIGHT)    
    
    puzzleWin.mainloop()