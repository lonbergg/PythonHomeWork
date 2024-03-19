class DictKeysIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.keys):
            key = self.keys[self.index]
            self.index += 1
            return key
        else:
            raise StopIteration



dictionary = {"a": 1, "b": 2, "c": 3}
dict_iter = DictKeysIterator(dictionary)
for key in dict_iter:
    print(key)