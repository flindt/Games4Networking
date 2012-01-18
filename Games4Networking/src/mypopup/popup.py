'''
Created on Jan 18, 2012

@author: art3
'''

import tkinter as tk

def currencyconv():
    print("what do you want to exchange")
    what = input()
    print("and how much")
    x = int(e.get())
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
 
def popout():
    
    other = tk.Toplevel()
    other.title("Victors Window")
    otherlabel = tk.Label(other, text='this is it', relief = tk.RIDGE)
    otherlabel.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)
    otherbutton = tk.Button(other, text='CLICK ME').pack(side=tk.TOP)
    otherbutton = tk.Button(other, text='NO,NO, CLICK ME').pack(side=tk.BOTTOM)
    
    e = tk.Entry(other)
    e.pack(side=tk.TOP)
    e.get()