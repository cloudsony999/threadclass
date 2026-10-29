import sys
print(sys.version)

import threading

print('let us find the running thread...')

print("currently running thread in python ",threading.current_thread().name)

if threading.current_thread() == threading.main_thread():
    print('The current thread is main thread')
else:
    print('The current thread is NOT main thread')