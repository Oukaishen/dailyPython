import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
print("a is ")
print(a)
print("b is ")
print(b)
print("concatenate is ")
# ValueError: all the input array dimensions except for the concatenation axis must match exactly
print(np.concatenate((a,b),axis = 0))
print(np.concatenate((a,b),axis = 1))