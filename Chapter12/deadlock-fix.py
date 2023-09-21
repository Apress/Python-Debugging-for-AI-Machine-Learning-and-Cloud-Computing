# deadlock-fix.py 

import time
import threading

cs1 = threading.RLock()
cs2 = threading.RLock()

def thread_func1():
    with cs1:
        time.sleep(1)
        with cs2:
            pass 

def thread_func2():
    with cs1:
        time.sleep(1)
        with cs2:
            pass

def main():
    thread1 = threading.Thread(target=thread_func1)
    thread2 = threading.Thread(target=thread_func2)
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
