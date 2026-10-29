from threading import *

from time import *

class MyThread:
    def prepare(self):
        self.task1()
        self.task2()
        self.task3()
                

    def task1(self):
        print('Boil milk and tea for 5 min ...',end=' ')
        sleep(5)
        print('task1 is DONE.....')
    def task2(self):
        print('Add sugar and again boil 4 2 min... ',end=' ')
        sleep(10)
        print('task2 is DONE.....')
    def task3(self):
        print('Filter and Serve...... ',end=' ')
        print('task3 is DONE.....')


obj=MyThread()

t=Thread(target=obj.prepare)
t.start()
    
