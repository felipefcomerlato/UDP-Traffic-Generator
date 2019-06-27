import socket
import sys
import time
import argparse

parser = argparse.ArgumentParser(description='UDP Send')
parser.add_argument('--ip_dest', "-i")
parser.add_argument('--port', "-p")
parser.add_argument('--rate', "-r")
  
args = parser.parse_args()

ip_dest = args.ip_dest
port = int(args.port)
rate = int(args.rate)

# Socket UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dest = (ip_dest, port)

pack = 1250 # in bytes (10x125 bytes)
sleep = 1/(rate/10) # To send N packets per second
sleep_rounded = round(sleep,5)

print("\n\n-----------------------------------------------")
print("Dest: %s | Port: %s | Rate: %s Kbits" % (str(args.ip_dest), str(args.port), str(args.rate)))
print("Sending UDP packets at ~%s Mbit/s" % (format(rate/1000)))
print("-----------------------------------------------\n\n")

while True:
  clientSocket.sendto(bytes(int(pack)), dest)
  time.sleep(sleep_rounded)

clientSocket.close()