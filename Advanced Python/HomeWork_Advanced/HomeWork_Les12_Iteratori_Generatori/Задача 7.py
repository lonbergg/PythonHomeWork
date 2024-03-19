class EvenRangeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.current = self.start if self.start % 2 == 0 else self.start + 1
        return self

    def __next__(self):
        if self.current <= self.stop:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration


even_nums = EvenRangeIterator(1, 10)
for num in even_nums:
    print(num)