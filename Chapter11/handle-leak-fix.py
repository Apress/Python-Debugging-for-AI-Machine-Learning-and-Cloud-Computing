# handle-leak-fix.py 

import time
import threading

def thread_func():
    foo()

def main():
    while True:
        thread = threading.Thread(target=thread_func)
        thread.start()
        time.sleep(0.01)
    
def foo():
    bar()

def bar(): 
    time.sleep(1)

if __name__ == "__main__":
    main()
