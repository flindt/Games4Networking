'''
Created on Jan 18, 2012

@author: art3
'''
import tkinter as tk

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.other = tk.Toplevel()
        self.other.title("Victors Window")
        self.otherlabel = tk.Label(self.other, text='This exchanges Kr to Euro and RON', relief = tk.RIDGE)
        self.otherlabel.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)
        self.otherbutton = tk.Button(self.other, text='EXCHANGE', command=self.buttonclick).pack(side=tk.TOP)
        self.otherbutton = tk.Button(self.other, text='QUIT', command=self.other.quit).pack(side=tk.BOTTOM)
        self.outputvalue = tk.StringVar()
        self.otherlabel1 = tk.Label(self.other, textvariable =self.outputvalue).pack(side=tk.BOTTOM)
        
        self.e = tk.Entry(self.other)
        self.e.pack(side=tk.TOP)
    
    def buttonclick(self):
        print ('so, you want to exchange', self.e.get(),'kr')
        x = int(self.e.get())
        euro = x*0.14
        ron = x*0.59
        print ('that means',euro, 'euros and', ron, 'rons')
        
        self.outputvalue.set(str(euro)+" euros")
        
        
        
        
        
    '''
    def currencyconv(self):
        print("what do you want to exchange")
        what = input()
        print("and how much")
        x = int(self.e.get())
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
    '''
if __name__ == '__main__':
    
    win = tk.Frame()
    win.pack()
    
    
    MyClass()
    
    win.mainloop( )