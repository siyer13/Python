vowels = ['a', 'e', 'i', 'o', 'u']
string = 'hello madam'

vw = [ch for ch in string if ch in vowels]
print(len(vw))
