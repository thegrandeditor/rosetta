@staticmethod
def greet(name: str):
    print("Hello, " + name)

class Base:
    def __init__(self, x: int):
        self.x = x

class Derived(Base):
    def get_x(self):
        return self.x

async def fetch_data():
    return 42

def outer(x):
    def inner(y):
        return x + y
    return inner

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

data = [1, 2, 3]
result = list(map(lambda x: x * 2, data))

greet("Rosetta")
d = Derived(10)
print(d.get_x())
print(factorial(5))
f = outer(5)
print(f(10))
