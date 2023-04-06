from scapy.all import Ether, ARP, srp

# ==============================================================================================
# If all the bits of a MAC address are set to 1 , it means that the packet is a broadcast and it
# should go to every device in the network. Scapy uses hexadecimal representation, so we
# will create the following variable to denote the broadcast address:
# ==============================================================================================
broadcast = "FF:FF:FF:FF:FF:FF"


# =================================================
# Create ether layer, with broadcast as destinition
# =================================================
ether_layer = Ether(dst=broadcast)


# [List of option ether layer]
# print(ls(Ether))


# ==========================================================================================
# Define ip range
# This represents that we want to scan all the devices starting with IP address
# 192.168.74.1 up to 192.168.74.255 . The last 8 bits are called a bitmask and
# represent the number of hosts we want to scan. Remember that an IP address is 32 bits,
# and we say here that we want to mask 24 bits, so the remaining 32-24 = 8 bits are
# addressable only, which means that we are only scanning the last 256 hosts in the network.
# ==========================================================================================
ip_range = '192.168.1.3'


# ==========================
# create an ARP layer packet
# ==========================
arp_layer = ARP(pdst=ip_range)


# ===============================================
# Create packet with ethernet layer and arp layer
# ===============================================
packet = ether_layer / arp_layer


# ===============================
# send this packet as a broadcast
# we can use the srp function
# ===============================
print ('\x1b[1;32;1mThis is packet for ether and ARP Layer\x1b[0m')
print(arp_layer.show())
print ('\x1b[1;32;1m===========================\x1b[0m')
ans, unans = srp(packet, timeout=2)


# ==========================================================================================
# srp returns both answered and unanswered packets. We are interested in answered
# packets from online devices only. Now, to get the IP addresses and MAC addresses of the
# online devices, we can write the following code. We can iterate over the answer to see the
# IP and corresponding MAC addresses:
# ==========================================================================================
print ('\x1b[1;32;1mThis is ans Layer\x1b[0m')
print(ans.show())
print ('\x1b[1;32;1m===========================\x1b[0m')

for snd, rcv in ans:
    ip = rcv[ARP].psrc
    mac = rcv[Ether].src
    print("IP = ", ip, " MAC = ", mac)