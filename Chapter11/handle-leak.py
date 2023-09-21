# handle-leak.py 

import time
import threading

def thread_func():
    foo()

def main():
    threads: list[threading.Thread] = []
    while True:
        thread = threading.Thread(target=thread_func)
        threads.append(thread)
        thread.start()
        time.sleep(1)
    
def foo():
    bar()

def bar(): 
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
