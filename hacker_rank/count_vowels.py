class CountVowels:

    vowels = []

    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']

    def count_vowels(self, given_string):
        count = 0
        for char in given_string:
            if char in self.vowels:
                count = count+1
        return count


cv = CountVowels()
print(cv.count_vowels('hello'))

