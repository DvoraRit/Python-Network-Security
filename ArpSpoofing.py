from scapy.all import *

s=sniff(filter="arp", count=5)
i=0

found=False
while (i<5 and found==False):
	count = 0
	for j in range(0,5):
		if(s[i]==s[j] and i!=j):
			count=count+1
	if(count>2):
		found=True
		index=i
	i=i+1

if(found==True):
	print(s[index], "is an ArpSpoofing!!!!!")
