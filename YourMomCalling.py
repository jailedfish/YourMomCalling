import socket
from threading import Thread
from tkinter import messagebox
from configparser import ConfigParser

bind_ip, passw = '', 0
threads = []


def dumpConf():
    global bind_ip, passw, port

    cfg = ConfigParser().read('config.ini')

    for x in cfg['CLIENT']['PASSWORD']:
        passw += ord(x)

    bind_ip = cfg['CLIENT']['BIND_ON']
    port = int(cfg['CLIENT']['PORT'])

def validateCon(con):
    data = con.resv(1024)
    if data.decode() != passw:
        con.sendall(b'e')
        return 1
    con.sendall(b's')
    return 0

def handleCon(con):
    if validateCon(con) != 0:
        return

    msgSent = False
    while not msgSent:
        data = con.resv(1024)

        if data.decode() == 'call':
            messagebox.showinfo('Your mom is calling', 'Get ready, pause the game!')
            msgSent = True
            con.close()

def waitThreads(thr):
    for x in thr:
        x.join()

def main():
    global threads

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((bind_ip, port))
    s.listen()
    

    while True:
        con, _ = s.accept()
        
        threads.append(Thread(target=handleCon, args=(con)))
        threads[-1].run()
try:
    dumpConf()
    CLIENT()
except:
    pass
finally:
    waitThreads(threads)



