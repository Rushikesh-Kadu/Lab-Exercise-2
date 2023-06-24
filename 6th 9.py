import pickle

f = open('file1.txt','wb')
dict = {1:"Jain",2:"Swaraj",3:"Vijay",4:"Aman"}
pickle.dump(dict,f)