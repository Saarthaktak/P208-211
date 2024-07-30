import socket
from  threading import Thread
import time
import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def ftp():
    global IP_ADDRESS
    authorizer = DummyAuthorizer()
    authorizer.adduser("lftpd","lftpd",".",perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = authorizer
    ftp_server = FTPServer(("IP_ADDRESS, 21"),handler())
    ftp_server.serve_forever


setup_thread = Thread(target=setup)           
setup_thread.start()

ftp_thread = Thread(target=ftp)               
ftp_thread.start()
