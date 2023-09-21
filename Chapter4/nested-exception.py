# nested-exception.py 

def main():
    foo()

def foo():
    bar()

def bar():
    try:
        raise Exception("Inner Exception")
    except Exception:
        raise Exception("Outer Exception")

if __name__ == "__main__":
    main()
