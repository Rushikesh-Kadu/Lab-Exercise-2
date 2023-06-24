fileName = input("Enter File Name:")
max_word = ''
max_word_len = 0
f = open(fileName,'r')
for line in f.readlines():
    for word in line.split(' '):
        if max_word_len<len(word):
            max_word =word
            max_word_len=len(word)
print(max_word)