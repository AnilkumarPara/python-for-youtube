import time
import numpy as np
start_time = time.time()
np.array(range(1, 100000))
end_time = time.time()
elapsed_time = end_time - start_time
print("Time taken to perform the function =", elapsed_time)
