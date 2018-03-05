import numpy as np

x = np.arange(8)
print(x)
print(np.array_split(x,3))

print(x)
# this will raise an error ValueError: array split does not result in an equal division
# print(np.split(x,3))