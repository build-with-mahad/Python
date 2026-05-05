import numpy as np
import time
rng = np.random.default_rng(seed=1)
flips = rng.integers(0,2, size=100000)
prob_heads = np.mean(flips) # 0 - tails , 1 - heads
print(f"Probability Heads : {prob_heads}")

start_time = time.time()
squares = [i**2 for i in range(1000000)]
end_time = time.time()
print("Loop Time : ",end_time - start_time)

start_time = time.time()
arr = np.arange(1000000)
squares_arr = arr**2
end_time = time.time()
print("Array Time : ",end_time - start_time)