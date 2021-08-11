import socket
s=socket.socket()
print("Socket created")
port=12345
s.bind(('',port))
print('socket binded to %s' %(port))
s.listen()
print('Socket is Listening')

while True:
    c,addr=s.accept()
    print('Got connection from ',addr)
    c.send(b'Thank you for connecting')
    c.close()
    
