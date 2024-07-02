import concurrent.futures
import time
import numpy as np

# Function to perform a CPU-intensive computation (Fibonacci calculation)
def compute(n):
    if n <= 1:
        return n
    else:
        return compute(n-1) + compute(n-2)

# Function to perform computation on each element of the array in serial
def serial_computation(array):
    print("On array", len(array))
    return [compute(x) for x in array]

# Function to perform computation using ThreadPoolExecutor
def threaded_computation(array, num_threads):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(compute, array))
    return results

# Function to perform computation using ProcessPoolExecutor
def multiprocessing_computation(array, num_processes):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(compute, array))
    return results

def main():
    # Creating an array of random integers for Fibonacci calculation
    array_size = 40  # Reduced array size due to increased computation complexity
    lower_limit = 20
    upper_limit = 35
    large_array = np.random.randint(lower_limit,upper_limit, array_size)  # Fibonacci calculations for numbers between lower and upper limit.

    # Serial computation
    start_time = time.time()
    serial_result = serial_computation(large_array)
    end_time = time.time()
    print(f"Serial computation time: {end_time - start_time} seconds")

    # Multiprocessing computation
    num_processes = 4  # You can adjust this based on your CPU
    start_time = time.time()
    multiprocessed_result = multiprocessing_computation(large_array, num_processes)
    end_time = time.time()
    print(f"Multiprocessed computation time with {num_processes} processes: {end_time - start_time} seconds")

    # Multithreaded computation
    num_threads = 4  # Adjust as needed
    start_time = time.time()
    threaded_result = threaded_computation(large_array, num_threads)
    end_time = time.time()
    print(f"Threaded computation time with {num_threads} threads: {end_time - start_time} seconds")

if __name__ == '__main__':
    main()
