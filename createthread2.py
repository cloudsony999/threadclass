from threading import Thread

class MyThread(Thread):
    def __init__(self,str):
        Thread.__init__(self)
        self.str=str
        print('I am cons....')
    def run(self):
        for _ in range(1,6):
            print(_)

t1=MyThread("AMITAVA")

t1.start()

t1.join()

