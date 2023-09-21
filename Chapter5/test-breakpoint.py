def main():
    foo()

def foo():
    bar()

def bar():
    while True:
        breakpoint()

if __name__ == "__main__":
    main()
