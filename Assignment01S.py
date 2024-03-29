# Queens College
# Internet and Web Technology (CSCI 355)
# Winter 2024
# Assignment 01S - Socket Programming, Server Side
# Essmer Sanchez
# Collaboration: Worked With Class

import socket


# [6] Write a programs Assignment2Server.py
# https://www.geeksforgeeks.org/socket-programming-python/
def run_server(port):
    # create a socket object
    s = socket.socket()
    print("Socket successfully created")
    # Next, bind to the port, but no IP so we can listen to requests from anywhere
    s.bind(('', port))
    print("socket binded to %s" % (port))
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
    # a forever loop until we interrupt it or an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        # send a thank you message to the client.
        c.send('Thank you for connecting'.encode())
        # Close the connection with the client
        c.close()
        break


def main():
    run_server(12345)


if __name__ == "__main__":
    main()
