from __future__ import print_function
import json, threading
from socket import *

DEBUG = True
ERROR = True
INFO = True


def debug(*args):
    if DEBUG:
        print("[DEBUG]",*args)

def info(*args):
    if info:
        print("[INFO]",*args)

def error(*args):
    if ERROR:
        print("[ERROR]",*args)


def jsonEncapsulate(data):
    try:
        data = json.dumps(data)
        return data
    except TypeError:
        error(data,"json Encode Error")
        return None

def jsonDecapsulate(data):
    try:
        data = json.loads(data)
        return data
    except json.decoder.JSONDecodeError:
        error("Error", data,"json Decode Error")
        return None



class lockedSocket(socket):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sendLock = threading.Lock()
        self.recvLock = threading.Lock()

    def accept(self):
        fd, addr = self._accept()
        sock = lockedSocket(self.family, self.type, self.proto, fileno=fd)
        if getdefaulttimeout() is None and self.gettimeout():
            sock.setblocking(True)
        return sock, addr
        