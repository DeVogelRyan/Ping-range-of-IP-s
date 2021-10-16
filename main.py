import os

def getInput():
    hostList = []
    start = input("Give a starter ip(example=192.168.1.2): ")
    end = int(input("Give a end host(example=5): "))
    hostList.append(start)
    hostList.append(end)
    StripLastPortion(hostList)

def StripLastPortion(hostList = []):
    bigPortion = []
    item = hostList[0]
    remove_dot = item.split(".")#split the ip in portions(example): 192.168.1.2 = [192, 168, 1, 2]
    for i in range(0,3):
        bigPortion.append(remove_dot[i])#add the first 3 portions to the list(example): [192, 168, 1]
    endPortion = int(remove_dot[3])# get the last portion(example): 2
    SendPings(bigPortion, endPortion, hostList[1])

def SendPings(host, min, max):
    IP = ""
    for portion in host:
        IP += (portion + '.')#reconstruct the Ip back to [192, 168, 1] = 192.168.1.

    for item in range(min, max+1):
        full_ip = IP + str(item)#add the last bit so 192.168.1. becomes 192.168.1.2
        response = os.system("ping -n 1 " + full_ip)#ping the ip in a loop
        if response == 1:
            print(item, 'is up!')
        else:
            print(item, 'is down!')

if __name__ == "__main__":
    getInput()