import numpy as np

x = np.arange(9)

print(x)

print(np.random.permutation(x))

# this will only permutate along the first axis
print(np.random.permutation(x.reshape(3,3)))


