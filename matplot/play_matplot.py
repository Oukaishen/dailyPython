import matplotlib.pyplot as plt
import numpy as np

# this is the first example form matplot
# https://matplotlib.org/tutorials/introductory/pyplot.html
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
# plt.show()

# now play with my data
X = np.array([[3,4,2,6,8,2,5],[5,5.5,4,7,10,5,7.5]])
# print("Original data is ")
# print(X)

# now i need a scatter plot
plt.figure()
plt.plot(X[0,:],X[1,:],"ro")
plt.show()