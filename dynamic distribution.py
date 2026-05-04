from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

data = list(range(1, 17))

def process_task(x):
    work_time = random.uniform(0.1, 0.5)  # beban tidak merata
    print(f"Proses {x} butuh {work_time:.2f} detik")
    time.sleep(work_time)
    return x * x

print("Dynamic distribution berjalan...\n")

start_time = time.time()

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(process_task, x) for x in data]

    for future in as_completed(futures):
        result = future.result()
        print(f"Hasil selesai: {result}")

end_time = time.time()

print(f"\nTotal waktu eksekusi: {end_time - start_time:.2f} detik")
