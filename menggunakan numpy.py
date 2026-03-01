import numpy as np
import multiprocessing as mp
import time
import os

# SERIAL VERSION
def serial_multiply(A, B):
    return np.dot(A, B)

# PARALLEL VERSION
def multiply_row(row, B):
    return np.dot(row, B)

def parallel_multiply(A, B, num_cores):
    with mp.Pool(num_cores) as pool:
        result = pool.starmap(multiply_row, [(row, B) for row in A])
    return np.array(result)


# MAIN PROGRAM
if __name__ == "__main__":
    N = 500  # ukuran matriks

    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    total_cores = os.cpu_count()
    print("Total CPU Cores:", total_cores)

    # ---- SERIAL ----
    start_serial = time.time()
    C_serial = serial_multiply(A, B)
    end_serial = time.time()

    serial_time = end_serial - start_serial
    print("Serial Time:", serial_time)

    # ---- PARALLEL ----
    num_cores_used = total_cores 
    print("Cores Used for Parallel:", num_cores_used)

    start_parallel = time.time()
    C_parallel = parallel_multiply(A, B, num_cores_used)
    end_parallel = time.time()

    parallel_time = end_parallel - start_parallel
    print("Parallel Time:", parallel_time)

    # ---- SPEEDUP ----
    speedup = serial_time / parallel_time
    print("Speedup:", speedup)

    # ---- VALIDASI ----
    print("Hasil sama:", np.allclose(C_serial, C_parallel))