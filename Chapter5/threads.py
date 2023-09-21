import time
import threading

def thread_func():
    foo()

def main():
    t1 = threading.Thread(target=thread_func)
    t1.start()
    t2 = threading.Thread(target=thread_func)
    t2.start()
    while True:
        time.sleep(1)    
    t1.join()
    t2.join()

def foo():
    bar()

def bar():
    while True:
        print("_")
        time.sleep(1)

if __name__ == "__main__":
    main()
