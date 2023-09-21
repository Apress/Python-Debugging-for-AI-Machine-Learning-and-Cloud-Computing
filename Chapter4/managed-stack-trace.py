# managed-stack-trace.py 

import traceback

def main():
    foo()

def foo():
    bar()

def managed_stack_trace(func):
    def call(*args, **kwargs):
        traceback.print_stack()
        return func(*args, **kwargs) 
    return call

@managed_stack_trace
def bar():
    print("Hello Traceback!")

if __name__ == "__main__":
    main()
