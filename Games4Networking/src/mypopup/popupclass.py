'''
Created on Jan 18, 2012

@author: art3
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        other = tk.Toplevel()
        other.title("Victors Window")
        otherlabel = tk.Label(other, text='this is it', relief = tk.RIDGE)
        otherlabel.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)
        otherbutton = tk.Button(other, text='CLICK ME').pack(side=tk.TOP)
        otherbutton = tk.Button(other, text='NO,NO, CLICK ME').pack(side=tk.BOTTOM)
        
        e = tk.Entry(other)
        e.pack(side=tk.TOP)
        e.get()