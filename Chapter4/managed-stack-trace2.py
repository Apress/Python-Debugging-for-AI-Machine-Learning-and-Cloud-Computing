# managed-stack-trace2.py 

import traceback
import inspect

def main():
    foo()

def foo():
    bar()

def managed_stack_trace(func):
    def call(*args, **kwargs):
        traceback.print_stack(f=inspect.currentframe().f_back)
        return func(*args, **kwargs) 
    return call

@managed_stack_trace
def bar():
    print("Hello Traceback!")

if __name__ == "__main__":
    main()
