import time
import threading 

def sanash1():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Marat: ")

def sanash2():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Tagaev: ")

def sanash3():
    for x in range(0, 30):
        time.sleep(0.2)
        print("Baqitjan ogli: ")

t1 = threading.Thread(target=sanash1)
t2 = threading.Thread(target=sanash2)
t3 = threading.Thread(target=sanash3)


t1.start()
t2.start()
t3.start()