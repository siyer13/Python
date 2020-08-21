import sys
from collections import OrderedDict

print("Enter Number: ")
count = int(sys.stdin.readline())
print("Enter Data: ")
words = []
word_appearence = OrderedDict()
for i in range(count):
    data = sys.stdin.readline()
    words.append(data.strip('\n'))

print(words)

print("Number of unique words")
unique_words = set(words)
print(len(unique_words))

for word in words:
    if word_appearence.get(word) is None:
        word_appearence[word] = 1
    else:
        value = word_appearence.get(word)
        value = value + 1
        word_appearence[word] = value

for key in word_appearence:
    print(word_appearence[key]),
