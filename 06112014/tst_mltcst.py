import socket
import struct
from time import sleep

MCAST_GRP = '224.0.0.0'
MCAST_PORT = 5007
print "mcasting configured"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
print "socket initialized"
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
print "setsockopt done"
sock.bind(('', MCAST_PORT))
print "bind with mcast_port done"
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
print "mreq = "
print mreq
sock.sendto('hii', (MCAST_GRP, MCAST_PORT))
print "'hii' sent"
#sleep(2)
rcv = sock.recv(10240)
print "recieved data:"
print(rcv)
