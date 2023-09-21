import time

class cls:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

def main():
    func = "main"
    while True:
        foo()
        time.sleep(1)

def foo():
    func = "foo"
    bar("argument")

def bar(arg):
    func = "bar"
    obj = [1, 2]
    obj = cls(1, 2)

if __name__ == "__main__":
    main()
