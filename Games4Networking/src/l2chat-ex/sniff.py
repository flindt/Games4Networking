'''
Created on Jan 19, 2012

@author: art3
'''
from scapy.all import Ether,sniff,sendp


sniff(prn=lambda x: "from %s -> %s" %(x.src, x['Raw'].load), lfilter=lambda x: x.haslayer(Ether) and x.fields['type'] == 0x8088)