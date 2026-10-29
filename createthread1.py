from threading import *

def display(name:str):
    print(name+' I am running!!!!!')




for i in range(10):
    t=Thread(target=display,args=('HELLO.....',))
    t.start()