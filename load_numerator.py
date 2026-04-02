import numpy as np

arr = np.load("hSeriesNumSimplified.npy", allow_pickle=True)

print("Shape:", arr.shape)
print("Dtype:", arr.dtype)
print("Example entry type:", type(arr.flat[0]))
