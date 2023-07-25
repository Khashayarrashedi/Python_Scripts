import sys
#--------------------------------------------------------------- CLASS JAR

class Jar:
    def __init__(self, _capacity=12):
        if _capacity < 0:
            raise ValueError("Out of range.")
        self._capacity = _capacity
        self._size = 0

    def __str__(self):
        return ("🍪" * self._size)

    def deposit(self, n):
        self._size= self._size + int(n)
        if 0 <= self._size <= self._capacity:
            pass
        else:
            raise ValueError("Out of _size.")

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Out of _size.")
        self._size -= n

    @property
    def capacity(self):
        if 0 <= self._capacity-self._size <= self._capacity:
            print(self._capacity-self._size)
            return (self._capacity-self._size)
        else:
            raise ValueError("Out of _size.")

    @property
    def size(self):
        super().__init__()
        print(self._size)
        return self._size


#--------------------------------------------------------------- MAIN
def main():

    jar= Jar(15)
    jar.deposit(10)
    jar.deposit(2)
    jar.withdraw(7)
    print(jar)
    # jar.capacity()
    # jar.size()

#--------------------------------------------------------------- MAIN CALL
if __name__ == "__main__":
    main()