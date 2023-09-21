# deadlock-exception.py 

import time
import threading
import logging

cs1 = threading.RLock()
cs2 = threading.RLock()

def foo (data):
    if data: raise "Exception" 

def thread_func1():
    try:
        cs1.acquire()
        foo(1)    
        cs1.release()
    except:
        logging.error("Exception logged")

    time.sleep(2)

    cs2.acquire()
    cs2.release()

def thread_func2():
    cs2.acquire()
    cs1.acquire()

    time.sleep(3)

    cs1.release()
    cs2.release()

def main():
    thread1 = threading.Thread(target=thread_func1)
    thread2 = threading.Thread(target=thread_func2)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
