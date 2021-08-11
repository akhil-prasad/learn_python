import time
import threading

def fun1(n):
    time.sleep(n)
    print('5 seconds')

def fun2(m):
    time.sleep(m)
    print("2 seconds")

t1= threading.Thread(target=fun1, args=(5,)) #tuple
t2= threading.Thread(target=fun2, args=(2,))


t1.start()
t2.start()
t1.join()
print("completed")
