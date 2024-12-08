# Libraries
import logging
from logging.handlers import RotatingFileHandler
import socket
from pyrsistent import b

# Constants
logging_format = logging.Formatter('%(message)s')

# Loggers & Logging Files
funnel_logger = logging.getLogger('FunnelLogger')
funnel_logger.setLevel(logging.INFO)    #To get information only 
funnel_handler = RotatingFileHandler('audits.log', maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)


creds_logger = logging.getLogger('CredsLogger')
creds_logger.setLevel(logging.INFO)    #To get information only 
creds_handler = RotatingFileHandler('cmd_audits.log', maxBytes=2000, backupCount=5)
creds_handler.setFormatter(logging_format)
creds_logger.addHandler(creds_handler)


#Emulated Shell
def emulated_shell(channel, client_ip):
    channel.send(b'imonU$ ')
    command = b""  #listening for user input
    while True:
        char = channel.recv(1)
        channel.send(char)
        if not char:
            channel.close()
