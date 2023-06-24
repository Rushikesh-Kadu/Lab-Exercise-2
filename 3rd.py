# A

# with open('file1.txt','r') as f:
#     f1 = open('file2.txt','w')
#     f1.writelines(f)
#     f1.close()


# B

# from string import punctuation

# special_symbol = set(punctuation)
# with open('file1.txt','r') as f:
#     char_len=0
#     symbol=0
#     file = f.read()
#     line_len = len(file.split('\n'))
#     for line in file:
#         if '\n' in line:
#             symbol+=1
#         char_len+=len(line)
#         for char in line:
#             if char in special_symbol:
#                 symbol+=1
    
#     print(line_len)
#     print(char_len)
#     print(symbol)
    


# 3
from threading import *
from string import punctuation

def copy():
    try:
        with open('file1.txt','r') as f:
            f1 = open('file2.txt','w')
            f1.writelines(f)
            f1.close()
    except:
        print("Something Went Wrong")

def count():
    special_symbol = set(punctuation)
    try:
        with open('file1.txt','r') as f:
            char_len=0
            symbol=0
            file = f.read()
            line_len = len(file.split('\n'))
            for line in file:
                if '\n' in line:
                    symbol+=1
                char_len+=len(line)
                for char in line:
                    if char in special_symbol:
                        symbol+=1        
        print(line_len)
        print(char_len)
        print(symbol)
    except:
        print("Something Went Wrong")
            
t1 = Thread(target=copy)
t2 = Thread(target=count)
t1.start()
t2.start()
            