class Jar:

    def __init__(self,capacity=12,size=0):
        if capacity<0:
            raise ValueError("invalid capacity")
        self._size=size
        self._capacity=capacity


    def __str__(self):
        return self._size * "🍪"
    def deposit(self,n):
        if n>self._capacity:
            raise ValueError("excceded")
        if self._size+n>self._capacity:
            raise ValueError("excceded")

        self._size+=n

    def withdraw(self,n):
        if self._size<n:
            raise ValueError("shortage of cookies:>")
        self._size-=n

    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size



jar=Jar()
jar.deposit(12)
jar.withdraw(10)
print(jar)

