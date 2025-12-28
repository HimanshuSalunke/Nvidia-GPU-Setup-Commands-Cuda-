import torch
import time

print("PyTorch version:", torch.__version__)
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("Using GPU:", torch.cuda.get_device_name(0))
else:
    print("No GPU found, exiting")
    exit()

# Large-scale matrix multiplication benchmark
matrix_size = 8192
iterations = 50

# Preallocate matrices on GPU
a = torch.randn((matrix_size, matrix_size), device=device)
b = torch.randn((matrix_size, matrix_size), device=device)

# Warm-up
_ = torch.matmul(a, b)

# Benchmark loop
torch.cuda.synchronize()  # Ensure warm-up finished
start = time.time()
for _ in range(iterations):
    c = torch.matmul(a, b)
torch.cuda.synchronize()  # Wait for all GPU ops
end = time.time()

avg_time = (end - start) / iterations
print(f"PyTorch GPU matmul {matrix_size}x{matrix_size} for {iterations} iterations")
print(f"Average time per iteration: {avg_time:.4f} seconds")
