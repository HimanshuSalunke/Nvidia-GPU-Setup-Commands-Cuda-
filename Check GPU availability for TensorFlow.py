import tensorflow as tf
import time

print("TensorFlow version:", tf.__version__)
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print("Num GPUs Available:", len(gpus))
    print("Using GPU:", gpus[0])
else:
    print("No GPU found, exiting")
    exit()

# Large-scale matrix multiplication benchmark
matrix_size = 8192  # larger matrices to stress GPU
iterations = 50     # repeat for more load

# Preallocate matrices
a = tf.random.normal((matrix_size, matrix_size))
b = tf.random.normal((matrix_size, matrix_size))

# Warm-up (first run is slower due to CUDA context initialization)
_ = tf.matmul(a, b)

# Benchmark loop
start = time.time()
for _ in range(iterations):
    c = tf.matmul(a, b)
end = time.time()

avg_time = (end - start) / iterations
print(f"TensorFlow GPU matmul {matrix_size}x{matrix_size} for {iterations} iterations")
print(f"Average time per iteration: {avg_time:.4f} seconds")
