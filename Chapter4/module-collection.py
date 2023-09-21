# module-collection.py 

import math
import mymodule

def main():
    foo()

def foo():
    bar()

def bar():
    mymodule.myfunc()
    math.sqrt(-1)

if __name__ == "__main__":
    try:
        main()
    except:
        import sys
        for name in sys.modules: 
            print(f"{sys.modules[name]}")
