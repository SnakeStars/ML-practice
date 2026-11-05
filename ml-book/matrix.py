import numpy as np

def construct_matrix(x, y):
    return np.concatenate((x.reshape(-1,1), y.reshape(-1,1)), axis=1)

print(construct_matrix(np.array([1,2,3]),np.array([4,5,6])))