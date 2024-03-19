class PalindromeIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            if word == word[::-1]:
                return word
        raise StopIteration


words_list = ['level', 'racecar', 'python', 'madam']
palindrome_iter = PalindromeIterator(words_list)
for word in palindrome_iter:
    print(word)