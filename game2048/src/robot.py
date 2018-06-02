'''
    This is interface that communicate between server and client GUI.
    It provides socketAPI functionalities and time measuring functionality.
    The protocol is to send size of the board and the board.

'''

import socket
import time
import random

class Robot:
    state = ''
    def __init__(self, host='35.187.230.213', port='50007'):
        self.host=host
        self.port=port

    def closeConn(self):
        self.socserv.close()


    def calNextMove(self, instate):
        if(self.state == instate):
            pass
        else:
            self.socserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socserv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socserv.connect((self.host, int(self.port)))

            sentstring = self.serializeState(instate)

            tsent = time.time()
            print("Sent :"+sentstring)
            print("At : "+time.strftime("%H:%M:%S", time.localtime(tsent)))
            self.socserv.sendall(bytes(sentstring,encoding='utf-8'));

            nextmove = self.socserv.recv(2048)
            trecv = time.time()
            print("Received :"+str(nextmove))
            print("At : "+time.strftime("%H:%M:%S", time.localtime(trecv)))

            ttotal = trecv-tsent

            print("Total Time Taken(s) : "+str(ttotal))
            #self.socserv.shutdown(socket.SHUT_RDWR)
            self.socserv.close()
            ## nextmove = self.emulateServer()

        return nextmove

    def pingServer(self):
        try:
            self.socserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socserv.connect((self.host, int(self.port)))
            self.socserv.close()
        except Exception:
            self.socserv.shutdown(socket.SHUT_RDWR)
            self.socserv.close()
            return 0

        return 1

    def emulateServer(self):
        moves = ["U", "D", "R", "L"]
        nextmove = moves[random.randint(0,3)]
        time.sleep(0.2)
        return nextmove

    def serializeState(self, instate):
        ## protocol = "boardsize, board[0][0] board[0][1] board[0]..."
        serialized = ''
        for i in range(len(instate)):
            for j in range(len(instate)):
                serialized = serialized+str(instate[i][j])+" "

        serialized = str(len(instate))+","+serialized

        return serialized



