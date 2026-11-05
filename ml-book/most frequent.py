import numpy as np

def most_frequent(nums):
    return np.bincount(nums).argmax()

print(most_frequent([1,2,4,4]))