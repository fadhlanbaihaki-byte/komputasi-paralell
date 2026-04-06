from concurrent.futures import ThreadPoolExecutor
import time

data = [5, 2, 9, 1, 7, 3]

def compute_average(data):
    print("Task1: Menghitung rata-rata...")
    time.sleep(0.5)  # Simulasi proses berat
    result = sum(data) / len(data)
    print(f"Task1 selesai = {result}")
    return result

def find_max(data):
    print("Task2: Mencari nilai maksimum...")
    time.sleep(0.5)
    result = max(data)
    print(f"Task2 selesai = {result}")
    return result

def sort_data(data):
    print("Task3: Melakukan sorting...")
    time.sleep(0.5)
    result = sorted(data)
    print(f"Task3 selesai = {result}")
    return result

# Eksekusi dengan ThreadPoolExecutor
print("="*50)
print("TASK PARALLELISM - EKSEKUSI PARALEL")
print("="*50)
start_time = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    future_avg = executor.submit(compute_average, data)
    future_max = executor.submit(find_max, data)
    future_sort = executor.submit(sort_data, data)
    
    avg = future_avg.result()
    max_val = future_max.result()
    sorted_data = future_sort.result()

print("="*50)
print("HASIL AKHIR:")
print(f"Average : {avg}")
print(f"Max     : {max_val}")
print(f"Sorted  : {sorted_data}")
print(f"Total waktu: {time.time() - start_time:.3f} detik")
print("="*50)

