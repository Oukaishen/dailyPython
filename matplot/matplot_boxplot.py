import matplotlib.pyplot as plt
import numpy as np

## the raw data of my box plot
X = np.array([[.801,.824,.841,.816,.840,.842,.820,.802,.828,.819],
              [121.41,127.70,129.20,131.80,135.10,131.50,126.7,115.1,130.8,124.6],
              [70.42,72.47,78.2,74.89,71.21,78.39,69.02,73.1,79.28,76.48]]).T

# print(X)

# draw the box plot
plt.boxplot(X[:,0],showmeans=True, meanline=True)
plt.show()