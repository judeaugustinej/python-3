import socket

def Main():
    host = '127.0.0.1'
    port = 5001

    # create a socket obj and bind a port to it.
    s = socket.socket()
    s.bind((host, port))

    # listen for one connection at a time
    s.listen(1)
    # accept the conection
    c, addr = s.accept()
    print("Connection from " + str(addr))

    # talk to the client
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From the connected user ", data)
        data = str(data).upper()
        print('Sending' , data)
        c.send(data.encode('utf-8'))

    c.close()

if __name__ == "__main__":
    Main()
