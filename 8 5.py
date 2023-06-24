import numpy as np

# a
# print(np.random.randint(0,15,size=(5,5)))


# b
# o=np.arange(0,101,21)
# print(o)

# c
# arr = np.array([1,2,3,4,5,6,7,8,9])
# arr.resize(3,3)
# print(arr)

#d
# arr = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
# print(arr.astype(int))


# e
# arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr2 = np.array([[11,22,33],[44,55,66],[77,88,99]])
# print(np.stack((arr1,arr2),axis=2))


# f
arr1 = np.array([1,2,3,4,5,6,7,8,9])
arr2 = np.array([1,22,33,4,55,66,77,88,99])
print(np.where(arr1==arr2))

