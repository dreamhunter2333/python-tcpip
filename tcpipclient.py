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
# 建立连接:
iptuple = (ip,com)
s.connect((iptuple))

def recv(i):
    while True:
        data=s.recv(1024).decode('utf-8')
        t.insert('1.0','接收数据: '+data+'\n')
        time.sleep(0.1)

def rec():
    for i in range(1, 1+1):
        th=threading.Thread(target=recv,args=(i,))
        th.setDaemon(True)#守护线程
        th.start()
    var.set('run')

def stop():
    var.set('stop')
    t.insert('1.0','---------------正在退出---------------\n')
    time.sleep(1)
    exit()

root = Tk()
root.title("多线程 by jinmu333")
root.geometry('400x600')                 #是x 不是*
root.resizable(width=True, height=True) #宽不可变, 高可变,默认为True
l = Label(root, text="反馈至idl253841@gmail.com", font=("Arial", 7), width=20)
l.pack(side=BOTTOM)
t = Text()
t.pack()
t.insert('1.0', "此处显示历史记录\n")
var = StringVar()
e = Entry(root, textvariable = var)
var.set('请在下方键入')
e.pack()
data=s.recv(1024).decode('utf-8')
var.set(data)
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.Button1 = Button(self, text='开始接收', command=rec,width = 20,height = 2,bd = 2)
        self.Button1.pack()
        self.nameInput = Entry(self)
        self.nameInput.bind('<Key-Return>',self.send)
        self.nameInput.pack()
        self.alertButton = Button(self, text='发送消息', command=self.send,width = 20,height = 2,bd = 2)
        self.alertButton.pack()
        self.stop = Button(self, text='退出', command=stop,width = 20,height = 2,bd = 2)
        self.stop.pack(side='right')

    def send(self,event):
        name = self.nameInput.get() or 'world'
        s.send(name.encode('ascii'))
        time.sleep(0.5)
'''     data=s.recv(1024).decode('utf-8')
        var.set(data)
        t.insert('1.0', "%s\n" %data)
'''

app = Application()

# 主消息循环:
app.mainloop()
