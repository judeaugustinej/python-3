import socket

def Main():
    host = '127.0.0.1'
    port = 5011
    # Creating a socket obj
    s = socket.socket()
    # and attach host and port to it.
    s.bind((host, port))

    # listen for one connection
    s.listen(1)
    c, addr = s.accept()
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "From user : " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == "__main__":
    Main()
