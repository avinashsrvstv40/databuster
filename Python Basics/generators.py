class generator:
    def __init__(self, n):
        self.n = n

    def square(self):
        for i in range(self.n):
            print("Yield has yet to be executed")
            yield i ** 2
            print("After yield has executoed")


if __name__ == "__main__":
    g = generator(10)

    for i in g.square():
        print(i)
