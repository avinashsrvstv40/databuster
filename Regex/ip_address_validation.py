import re

if __name__ == "__main__":
    
    ipv4 = "^(([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5][0-5])\.){3}([0-9]|[0-9]{2}|1[0-9]{2}|2[0-5][0-5])$"
    ipv6 = "^([0-9a-f]{1,4}:){7}[0-9a-f]{1,4}$"

    for _ in range(int(input())):
        string = input()
        if re.findall(ipv4, string):
            print("IPv4")
        elif re.findall(ipv6, string):
            print("IPv6")
        else:
            print("Neither")