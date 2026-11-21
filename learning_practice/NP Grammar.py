import numpy as np

# 1. Create Arrays
# 1.1 Create from lists
arr = np.array([1, 2, 3, 4])
arr2d = np.array([[1, 2], [3, 4]])  # Fixed: Added inner brackets

# 1.2 Special Arrays
# 2x3 array of zeros
zeros_arr = np.zeros((2, 3))
# Array of ones
ones_arr = np.ones((2, 3))
# Array filled with 5
full_arr = np.full((2, 3), 5)
# 3x3 Identity matrix
eye_arr = np.eye(3)
# Start, stop, step
arange_arr = np.arange(0, 10, 2)
# 5 evenly spaced points between 0 and 1
linespace_arr = np.linspace(0, 1, 5)
# Uniform random in [0, 1)
rand_arr = np.random.rand(3, 4)
# Standard normal random
randn_arr = np.random.randn(3, 4)

# 2. Shape and Reshaping
print("arr shape:", arr.shape)
print("arr ndim:", arr.ndim)
print("arr size:", arr.size)

reshape_arr = arr2d.reshape(4, 1)
flat_arr = arr2d.flatten()

# 3. Indexing and Slicing
# Extract a single element
val1 = arr[0]
# 1D slicing
slice_arr = arr[1: 3]
# 2D array element access
val2 = arr2d[0, 1]
# 2D array slicing
col0 = arr2d[:, 0]
# Boolean indexing / Conditional filtering
mask_arr = arr[arr > 2]

# 4. Mathematical Operations
arr_plus = arr + 1
# Element-wise addition
arr_add = arr + arr
sum_val = np.sum(arr)
# Calculate mean
mean_val = np.mean(arr)
max_val = np.max(arr)
min_val = np.min(arr)
sqrt_arr = np.sqrt(arr)
sin_arr = np.sin(arr)
# Standard deviation (measures data dispersion; larger values mean higher volatility)
std_val = np.std(arr)

# 5. Array Concatenation
# Vertical concatenation (along rows)
concat_v = np.concatenate([arr2d, arr2d], axis=0)
# Horizontal concatenation (along columns)
concat_h = np.concatenate([arr2d, arr2d], axis=1)