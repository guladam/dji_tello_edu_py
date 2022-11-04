import threading 
import socket
import sys
import time

host = ''
port = 9000
locaddr = (host, port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)

tello_address = ('192.168.10.1', 8889)
COMMANDS = []
ALL_COMMANDS = 0
NEXT = True

def _recv():
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            ans = data.decode(encoding="utf-8")
            print(ans)
            
            if ans == "ok":
                time.sleep(1)
                global NEXT
                NEXT = True
                
        except Exception:
            print ('\Landolás . . .\n')
            break

#recvThread create
recvThread = threading.Thread(target=_recv)
recvThread.start()

def elore(n):
    COMMANDS.append(f"forward {n}")


def hatra(n):
    COMMANDS.append(f"back {n}")


def fel(n):
    COMMANDS.append(f"up {n}")


def le(n):
    COMMANDS.append(f"down {n}")


def jobbra(alfa):
    COMMANDS.append(f"cw {alfa}")


def balra(alfa):
    COMMANDS.append(f"ccw {alfa}")


def szalto():
    COMMANDS.append("flip f")


def hatra_szalto():
    COMMANDS.append("flip b")


def allj():
    COMMANDS.append("stop")


def inditas():
    COMMANDS.append("command")
    COMMANDS.append("takeoff")


def leallitas():
    COMMANDS.append("land")
    COMMANDS.reverse()
    
    global ALL_COMMANDS
    ALL_COMMANDS = len(COMMANDS)
    
    start()


def start():
    while len(COMMANDS) >= 1:
        global NEXT
        if NEXT:
            NEXT = False
            current = COMMANDS.pop()
            msg = current.encode(encoding="utf-8") 
            sent = sock.sendto(msg, tello_address)
            print(f"{ALL_COMMANDS - len(COMMANDS)}. parancs végrehajtása ({current}):", end=" ")
            
    print('A program véget ért.')
    sock.close()
