# -*- coding: utf-8 -*-

__author__ = 'jinmu333'

from tkinter import *
from multiprocessing import Process
import tkinter.messagebox as messagebox
import urllib,hashlib
import random
import requests,sys
import requests
import threading
import time
import socket

ip=input('请输入ip 回车默认:127.0.0.1') or '127.0.0.1'
com=input('请输入端口 回车默认:9999') or 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
iptuple = (ip,com)
s.bind((iptuple))
s.listen(5)
print('Waiting for connection...')
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        print(data)
        time.sleep(0.3)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
        time.sleep(0.3)
        sock.send(('tcpip' ).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()