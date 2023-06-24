fileName = input("Enter File Name:")
f = open(fileName,'r')
data = f.readlines()
content = ''.join(data)
for line in data:
    s = set(line)
    for element in s:
        print(element,'  ',content.count(element))