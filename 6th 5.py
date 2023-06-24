content= ''
with open('file2.txt','r') as f:
    for line in f.readlines():
        content+=line.replace('#','')

f1=open('file2.txt','w')
f1.writelines(content)
f1.close()