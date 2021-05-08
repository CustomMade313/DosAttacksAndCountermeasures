def parse_out_data(f: str):
    data = []
    packet = []  # [packets captured, packets filtered, packets dropped]
    with open(f) as f:
        for num, line in enumerate(f):
            if num == 2:
                data = line.split()
                packet.append(int(data[0]))
            if num == 3:
                data = line.split()
                packet.append(int(data[1]))
            if num == 4:
                data = line.split()
                packet.append(int(data[2]))
    return packet

                
parse_out_data("/home/plebeian_dev/Documents/Git Repos/DosAttacksAndCountermeasures/dos_src/out2")
