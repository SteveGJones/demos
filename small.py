import threading
import time
import random

class Foo:

    def __init__(self):
        self.bar = None

class SNA(threading.Thread):
    def __init__(self, foo):
        threading.Thread.__init__(self)
        self.foo = foo
        self.runme = True

    def pretendToDoSomething(self):
        #pause
        time.sleep(random.randrange(1,21,3))
        self.foo.bar = time.time()
        #like we are doing something
        self.elapsedInMillisconds = int((time.time() - self.foo.bar)*1000)
        return self.elapsedInMillisconds

    def run(self):
        while (self.runme):
            self.pretendToDoSomething()

class FU(threading.Thread):
    def __init__(self, foo):
        threading.Thread.__init__(self)
        self.foo = foo
        self.runme = True

    def pretendToDoSomething(self):
        #pause
        time.sleep(random.randrange(1,21,5))
        self.foo.bar = [time.time()]
        #like we are doing something
        self.foo.bar.append(time.time())
        self.elapsedInMillisconds = int((self.foo.bar[1] - self.foo.bar[0]) * 10000)
        return self.elapsedInMillisconds

    def run(self):
        while (self.runme):
            self.pretendToDoSomething()
    

def main():
    foo = Foo()
    sna = SNA(foo)
    fu = FU(foo)

    sna.start()
    fu.start()

if __name__ == "__main__":
    main()
