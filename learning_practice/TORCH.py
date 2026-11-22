import torch

# 1. Tensor Creation (Similar to NumPy)
# 1.1 Create from lists
tensor_1d = torch.tensor([1, 2, 3, 4])
tensor_2d = torch.tensor([[1, 2], [3, 4]])


# 1.2 Special Tensors
# 2x3 tensor of zeros
zeros_t = torch.zeros((2, 3))
# Tensor of ones
ones_t = torch.ones((2, 3))
# Tensor filled with 5
full_t = torch.full((2, 3), 5)
# 3x3 Identity matrix
eye_t = torch.eye(3)
# Start, stop, step (Note: step must be an integer in PyTorch)
arange_t = torch.arange(0, 10, 2)
# 5 evenly spaced points between 0 and 1
linspace_t = torch.linspace(0, 1, 5)
# Uniform random in [0, 1)
rand_t = torch.rand(3, 4)
# Standard normal random
randn_t = torch.randn(3, 4)


# 2. Shape and Reshaping
print("tensor_1d shape:", tensor_1d.shape)
print("tensor_1d dim:", tensor_1d.dim())     # dimension
print("tensor_1d numel:", tensor_1d.numel()) # number of elements

# reshape vs view: view() requires contiguous memory, reshape() is more flexible
reshape_t = tensor_2d.reshape(4, 1)
view_t = tensor_2d.view(4, 1)
flat_t = tensor_2d.flatten()


# 3. Indexing and Slicing
# Extract a single element (returns a 0-dim tensor)
val1 = tensor_1d[0]
# 1D slicing
slice_t = tensor_1d[1:3]
# 2D tensor element access (row 0, col 1)
val2 = tensor_2d[0, 1]
# 2D tensor slicing (all rows, col 0)
col0 = tensor_2d[:, 0]
# Boolean indexing / Conditional filtering
mask_t = tensor_1d[tensor_1d > 2]


# 4. Mathematical Operations
t_plus = tensor_1d + 1
# Element-wise addition
t_add = tensor_1d + tensor_1d
sum_val = torch.sum(tensor_1d)
mean_val = torch.mean(tensor_1d.float()) # Mean requires float type
# Note: torch.max() returns a namedtuple (values, indices)
max_val = torch.max(tensor_1d).values 
min_val = torch.min(tensor_1d).values
sqrt_t = torch.sqrt(tensor_1d.float())
sin_t = torch.sin(tensor_1d.float())
std_val = torch.std(tensor_1d.float())

# Matrix Multiplication (Dot product)
# Note: '*' is element-wise multiplication, use '@' or torch.matmul() for matrix multiplication
dot_val = torch.matmul(tensor_2d, tensor_2d) 
dot_val_short = tensor_2d @ tensor_2d


# 5. Tensor Concatenation and Stacking
# Vertical concatenation (along dimension 0, like np.concatenate)
concat_v = torch.cat([tensor_2d, tensor_2d], dim=0)
# Horizontal concatenation (along dimension 1)
concat_h = torch.cat([tensor_2d, tensor_2d], dim=1)
# Stacking: creates a NEW dimension (results in a 3D tensor here)
stack_t = torch.stack([tensor_2d, tensor_2d], dim=0)


# 6. PyTorch Specifics: Device & Autograd (Core Features)
# 6.1 Device Management (CPU vs GPU)
device = "cuda" if torch.cuda.is_available() else "cpu"
tensor_gpu = tensor_1d.to(device)
print(f"Current device: {device}")

# 6.2 Automatic Differentiation (Autograd)
# requires_grad=True tells PyTorch to track operations on this tensor
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x ** 2 + 2 * x
# Compute gradients (dy/dx) using backpropagation
y.sum().backward() 
print("Gradient (dy/dx):", x.grad) # Output will be [6.0, 8.0] (since 2x+2)
