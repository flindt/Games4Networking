'''
Created on Jan 19, 2012

@author: art3
'''

from scapy.all import Ether,sniff,sendp

a=Ether()
a.type=0x8088
a.src='cc:52:af:0e:2c:c2'

while True:
    print("say something, and be sure to add quotation marks")

    data = 'victor says : ' + input()

    b=a/data

    sendp(b, count=2, iface='wlan0')
