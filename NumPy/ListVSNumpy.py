import numpy as np
import time

a = np.random.rand(1000000000)

# List
# start = time.time()
# by_list = sum(a)/len(a)
# result = time.time()-start
# print(result)  # it took approx 178 sec

# np
start = time.time()
by_np = np.mean(a)
result = time.time()-start
print(result)
