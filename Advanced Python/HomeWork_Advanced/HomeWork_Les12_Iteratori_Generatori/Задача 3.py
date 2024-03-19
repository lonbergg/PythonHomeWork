class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.string):
            char = next(iter(self.string[self.index]))
            self.index += 1
            return char
        else:
            raise StopIteration


string = "Hello, World!"
str_iter = StringIterator(string)
for char in str_iter:
    print(char)