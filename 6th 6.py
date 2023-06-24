content = ''
with open('data.txt','r') as f:
    for line in f.readlines():
        for word in line.split(' '):
            content+=word[::-1]+' '

f1 = open('data1.txt','w')
f1.writelines(content)
f1.close()