with open('file1.txt','r') as f:
    character = 0
    digit = 0
    special_symbol = 0
    word = 0
    space = 0
    line_len = 0
    for line in f:
        line_len+=1
        word+=len(line.split(' '))
        space+=line.count(' ')
        for char in line:
            if char>='0' and char<='9':
                digit+=1
            elif char>='A' and char<='z':
                character+=1
            else:
                special_symbol+=1        


print(character)
print(digit)
print(special_symbol)
print(word)
print(space)
print(line_len)


#2
print(__file__)