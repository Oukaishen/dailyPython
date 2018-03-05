import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,2,2,2])
print(np.where((a != 2) & (b == 2))[0])