def my_decorator(func):
    return func

class Base:
    def greet(self):
        return "Hello"

class Derived(Base):
    @my_decorator
    async def process_data(self, items: list) -> list:
        # List comprehension
        result = [x * 2 for x in items if x > 0]
        return result

    def my_generator(self):
        yield 1
        yield 2

async def main():
    d = Derived()
    print(await d.process_data([1, 2, -1]))
