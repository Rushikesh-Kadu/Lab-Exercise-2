import csv

with open('file11.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['Category','Winner','Film','Year'])
    n=int(input("Enter How many no of data u want to Enter:"))
    for i in range(n):
        cat = input("Enter Category:")
        win = input("Enter Winner:")
        film = input("Enter Film:")
        year = input("Enter Year:")
        w.writerow([cat,win,film,year])
print(n,"Record added Successfully")