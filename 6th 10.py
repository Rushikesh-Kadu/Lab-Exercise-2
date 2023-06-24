import csv

with open('temp_file.csv','w') as f:
    w=csv.writer(f)
    w.writerow(['Roll','Name','Unit Test1','Unit Test2','Unit Test3','Unit Test4','Unit Test5','Assignment1','Assignment2','Midterm(30)','Prelim(50)','Total(150)'])
    n = int(input("How many students data u want to Enter:"))
    for i in range(n):
        roll = int(input("Enter Roll No:"))
        Name = input("Enter Name:")
        test1 = int(input("Enter Test 1 Mark(out of 10):"))
        test2 = int(input("Enter Test 2 Mark(out of 10):"))
        test3 = int(input("Enter Test 3 Mark(out of 10):"))
        test4 = int(input("Enter Test 4 Mark(out of 10):"))
        test5 = int(input("Enter Test 5 Mark(out of 10):"))
        ass1 = int(input("Enter Assignment1 Marks(out of 10):"))
        ass2 = int(input("Enter Assignment2 Marks(out of 10):"))
        mid = int(input("Enter MidTerm Marks(out of 30):"))
        pre = int(input("Enter Prelim Marks(out of 50):"))
        total = test1+test2+test3+test4+test5+ass1+ass2+mid+pre
        w.writerow([roll,Name,test1,test2,test3,test4,test5,ass1,ass2,mid,pre,total])
print(n,"Students data have write successfully")
        