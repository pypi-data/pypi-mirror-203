from netpack.func import NetPack

ips = ['110.242.68.66', '180.240.192.138']
results = NetPack.multiple_ping(ips, 64, "icmp", 0.1, 1, 50)
print(results)
