import subprocess

# Set the interface
interface = 'wlan0'

# Set the new MAC address
new_macaddress = '12:34:56:78:90:01'

# First information about running script
print("Change MAC addres of interface \x1b[1;32;1m%s\x1b[0m to \x1b[1;31;1m%s\x1b[0m"%(interface, new_macaddress))

# Shutdown the interface
print ('shutdown the interface \x1b[1;31;1m%s\x1b[0m' %(interface))

subprocess.run(['ifconfig',interface, 'down'])

print ('\x1b[1;32;1m%s\x1b[0m'%('Changing process'))

subprocess.run( ['ifconfig', interface, 'hw', 'ether', new_macaddress])

print ('MAC address change to \x1b[1;32;1m%s\x1b[0m'%(new_macaddress))

subprocess.run(["ifconfig", interface, "up"])

print("network interfaced turned \x1b[1;32;1m%s\x1b[0m"%("On"))

try:
    while True:
            pass
except KeyboardInterrupt:
    print("\nStarting to change the real MAC address")

    print("Get the real MAC address ",end="")
    
    
    realone = subprocess.run(["ethtool -P wlan0 | awk '{print $3}'"], shell=True, capture_output=True).stdout.decode().replace("\n","")

    print(f"\nThe Real MAC Address {realone}")

    print("Turn down wlan interface")

    subprocess.run(["ifconfig",interface,"down"])

    print("\tWLAN is Down")

    print("Change MAC address")

    subprocess.run ("ifconfig wlan0 hw ether "+realone, shell=True)

    print("\t Done")

    print("Turnin on interface again")

    subprocess.run(["ifconfig wlan0 up"], shell=True)
