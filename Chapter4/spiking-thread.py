# spiking-thread.py 

import time
import threading
import math

def thread_func(spike):
    foo(spike)

def main():
    threads: list[threading.Thread] = []
    threads.append(threading.Thread(target=thread_func, args=[False]))
    threads.append(threading.Thread(target=thread_func, args=[True]))
    threads.append(threading.Thread(target=thread_func, args=[False]))
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def foo(spike):
    bar(spike)

def bar(spike):
    while True:
        if spike:
            math.sqrt(2);
        else:     
            time.sleep(1)

if __name__ == "__main__":
    main()
