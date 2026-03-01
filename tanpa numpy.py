import multiprocessing as mp
import time
import random
import os


# BUAT MATRIX RANDOM (LIST BIASA)
def generate_matrix(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

# SERIAL MATRIX MULTIPLICATION
def serial_multiply(A, B, n):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result

# PARALLEL HELPER (HITUNG 1 BARIS)
def multiply_row(args):
    row_index, A, B, n = args
    row_result = []

    for j in range(n):
        total = 0
        for k in range(n):
            total += A[row_index][k] * B[k][j]
        row_result.append(total)

    return row_result



# PARALLEL MATRIX MULTIPLICATION
def parallel_multiply(A, B, n, num_cores):
    with mp.Pool(num_cores) as pool:
        result = pool.map(
            multiply_row,
            [(i, A, B, n) for i in range(n)]
        )
    return result

# MAIN
if __name__ == "__main__":
    N = 500 

    print("Matrix size:", N, "x", N)

    A = generate_matrix(N)
    B = generate_matrix(N)

    total_cores = os.cpu_count()
    print("Total CPU Cores:", total_cores)

    # ---- SERIAL ----
    start_serial = time.time()
    C_serial = serial_multiply(A, B, N)
    end_serial = time.time()

    serial_time = end_serial - start_serial
    print("Serial Time:", serial_time)

    # ---- PARALLEL ----
    num_cores_used = total_cores
    print("Cores Used:", num_cores_used)

    start_parallel = time.time()
    C_parallel = parallel_multiply(A, B, N, num_cores_used)
    end_parallel = time.time()

    parallel_time = end_parallel - start_parallel
    print("Parallel Time:", parallel_time)

    # ---- SPEEDUP ----
    speedup = serial_time / parallel_time
    print("Speedup:", speedup)

    # ---- VALIDASI ----
    print("Hasil sama:", C_serial == C_parallel)