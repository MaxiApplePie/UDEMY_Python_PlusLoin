class CustomRange:
    def __init__(self, maximum):
        self.i = 1
        self.maximum = maximum

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.maximum:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


a = CustomRange(10)
print(a.__next__())
print(a.__next__())
print(a.__next__())
for z in a:
    print(z)
