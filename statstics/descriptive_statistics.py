import numpy as np

## this is the sample data
X = np.array([[42,4],[52,5],[48,4],[58,3]])
# print(X)

# calculate the mean
data_mean = np.mean(X,axis= 0)
# print(data_mean)

# calculate the covariance matrix
data_cov = np.cov(X,rowvar=False,bias=True)
# print("The covariance matrix is")
# print(data_cov)

# calculate the correlation matrix
data_cor = np.corrcoef(X,rowvar=False)
# print("The correlation matrix is")
# print(data_cor)