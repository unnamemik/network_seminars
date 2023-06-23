import socket
import threading

def read_sok():
     while True:
         data = sock.recv(1024)
         print(data.decode('utf-8'))

server = '192.168.0.107', 55444
alias = 'Mike: '
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 0))
sock.sendto(str.encode(alias+'connected'), server)

trd = threading.Thread(target= read_sok)
trd.start()

while True :
    msg = input()
    sock.sendto(str.encode(alias+msg), server)
