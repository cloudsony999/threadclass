from threading import *

from time import *


class Cinema:
    def __init__(self,str):
        self.str=str
    def movieshow(self):
        for i in range(1,6):
            print(self.str," : ",i)
            sleep(2)

obj1=Cinema('CUT THE TICKET')
obj2=Cinema('SHOW THE CHAIR TO SIT!!!!')


t1=Thread(target=obj1.movieshow)
t2=Thread(target=obj2.movieshow)

t1.start()
t2.start()

