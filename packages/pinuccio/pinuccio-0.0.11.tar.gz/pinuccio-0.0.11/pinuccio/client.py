from . import utils
from . import interface as sc
import socket, threading


class Client():
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        self.socket = None

    def start(self):
        self.socket = utils.lockedSocket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.IP, self.PORT))


    def send(self, data, key=None):
        """return True if message was sent without errors else False"""
        if self.socket:
            data = utils.jsonEncapsulate(data)
            if data:
                utils.info("send:", data)
                self.socket.sendLock.acquire()
                sc.msg_send(self.socket, data)
                self.socket.sendLock.release()
                return True
            else:
                return False
        return False

    def recv(self, key=None):
        """return None if socket is closed else return readed data"""
        if self.socket:
            # socket read
            try:
                self.socket.recvLock.acquire()
                data = sc.msg_recv(self.socket)
                utils.info("recv:", data)
            except Exception as e:
                utils.error(e,"Socket Error")
                self.close()
                return None
            finally:
                self.socket.recvLock.release()

            # encode from string to dict
            data = utils.jsonDecapsulate(data)
            if not data:
                return self.recv(self.socket, key)
            
            # if present msg field encode from string to dict 
            data = self.DecapsulateMessage(data)

            # if message is chek socket skip it
            if self.isCheckSocket(data): 
                return self.recv()
            
            return data
        return None
    
    def checkSocket(self, conn, to="None"):
        self.send(self.socket, {"action":"checkSocket"})

    def isCheckSocket(self, data):
        if "action" in data:
            if data["action"]=="checkSocket":
                return True
        return False

    def DecapsulateMessage(self, data):
        if "action" in data:
            if data["action"] == "msg":
                msg = utils.jsonDecapsulate(data["msg"])
                if msg:
                    data["msg"] = msg
        return data


    #Actions
    def close(self):
        if self.socket:
            try:
                self.send({"action":"close"})
                self.socket.close()
            finally:
                self.socket = None

    def subscribe(self, name=""):
        if self.socket:
            result = False
            if name=="":
                result = self.send({"action":"subscribe"})
            else:
                result = self.send({"action":"subscribe", "name":name})
            if not result:
                return False

            data = self.recv()
            if "status" in data:
                if data["status"]==200:
                    return True
        return False

    def getClients(self):
        if self.socket:
            self.send({"action":"getClients"})
        return False

    def sendMessage(self, msg, to):
        msg = utils.jsonEncapsulate(msg)
        self.send({"action":"send","msg":msg,"to":to})

    
    