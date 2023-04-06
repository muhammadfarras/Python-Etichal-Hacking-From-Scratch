from scapy.all import ICMP
from scapy.all import IP
from scapy.all import sr1
from scapy.all import ls

src_ip = '192.168.1.16'

dest_ip = 'www.anakshalihbogor.sch.id'


print ('Source ip address are \x1b[1;32;1m%s\x1b[0m and the target are \x1b[1;31;1m%s\x1b[0m' %(src_ip,dest_ip))

ip_layer = IP(
    src = src_ip,
    dst = dest_ip
)

# print(ip_layer.show())


# =================
# Send ICMP request
# =================

icmp_req = ICMP(id=100)
# print(icmp_req.show())


# =======================================
# Combine ip_layer with icmp_req
# This will list out the combined packet.
# =======================================

packet = ip_layer / icmp_req
# print(packet.show())


# ============
# sent request
# ============

# response = sr1(packet, iface = 'eth0')

# if response:
#     print (response.show())


# ===================================================================================
# If you want to see more details about a certain layer in Scapy and what options are
# available in the layer to modify, you can use the ls function in Scapy
# ===================================================================================

ip_layer_ls = IP(dst = dest_ip)
print(ls(ip_layer))


# =========================================================================================
# If you want to access the individual field of any layer, you can simply use the dot ( . )
# operator. For example, if you want to print dst in ip_layer , you can write the following
# code:
# =========================================================================================

# print("Destination : ", ip_layer_ls.dst)