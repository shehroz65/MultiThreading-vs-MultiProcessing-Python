import concurrent.futures
import time
import numpy as np
import os
import matplotlib.pyplot as plt
import logging

# Setup logging
logging.basicConfig(filename='performance_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Optimized function to perform a CPU-intensive computation (Fibonacci calculation)
# Function BigO: O(n)
def compute_opt(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Function to perform a CPU-intensive computation (Fibonacci calculation)
# Function BigO: O(2^n)
def compute(n):
    if n <= 1:
        return n
    else:
        return compute(n-1) + compute(n-2)

# Function to perform computation on each element of the array in serial
def serial_computation(array):
    logging.info(f"Running serial computation on array of size {len(array)}...")
    result = [compute(x) for x in array]
    logging.info("Serial computation completed.")
    return result

# Function to perform computation using ThreadPoolExecutor
def threaded_computation(array, num_threads):
    logging.info(f"Running threaded computation with {num_threads} threads on array of size {len(array)}...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(compute, array))
    logging.info("Threaded computation completed.")
    return results

# Function to perform computation using ProcessPoolExecutor
def multiprocessing_computation(array, num_processes):
    logging.info(f"Running multiprocessing computation with {num_processes} processes on array of size {len(array)}...")
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(compute, array))
    logging.info("Multiprocessing computation completed.")
    return results

# Function to measure execution time of a given computation method
def measure_time(func, array, *args):
    logging.info(f"Measuring time for {func.__name__}...")
    start_time = time.time()
    result = func(array, *args)
    end_time = time.time()
    duration = end_time - start_time
    logging.info(f"{func.__name__} took {duration:.4f} seconds.\n")
    return duration, result

def main():
    # Configuration
    array_sizes = [20, 30, 40]
    lower_limit = 20
    upper_limit = 35
    num_runs = 5
    num_threads = 4
    num_processes = min(4, os.cpu_count())

    # Store results for plotting
    serial_times = []
    threaded_times = []
    multiprocessing_times = []

    logging.info("Starting performance comparison...\n")

    for size in array_sizes:
        logging.info(f"\n=== Testing with array size {size} ===")
        serial_time_sum = 0
        threaded_time_sum = 0
        multiprocessing_time_sum = 0

        for run in range(num_runs):
            logging.info(f"\n--- Run {run + 1} of {num_runs} for array size {size} ---")
            # Create a random array for Fibonacci calculation
            large_array = np.random.randint(lower_limit, upper_limit, size)
            logging.info(f"Generated array: {large_array}\n")

            # Serial computation
            time_taken, serial_result = measure_time(serial_computation, large_array)
            serial_time_sum += time_taken

            # Threaded computation
            time_taken, threaded_result = measure_time(threaded_computation, large_array, num_threads)
            threaded_time_sum += time_taken

            # Multiprocessing computation
            time_taken, multiprocessing_result = measure_time(multiprocessing_computation, large_array, num_processes)
            multiprocessing_time_sum += time_taken

            # Ensure results are consistent
            assert serial_result == threaded_result == multiprocessing_result, "Results are not consistent across methods!"
            logging.info("Results are consistent across all methods.\n")

        # Average the times over the number of runs
        avg_serial_time = serial_time_sum / num_runs
        avg_threaded_time = threaded_time_sum / num_runs
        avg_multiprocessing_time = multiprocessing_time_sum / num_runs

        serial_times.append(avg_serial_time)
        threaded_times.append(avg_threaded_time)
        multiprocessing_times.append(avg_multiprocessing_time)

        logging.info(f"\n--- Averages for array size {size} ---")
        logging.info(f"Average serial computation time: {avg_serial_time:.4f} seconds")
        logging.info(f"Average threaded computation time: {avg_threaded_time:.4f} seconds")
        logging.info(f"Average multiprocessing computation time: {avg_multiprocessing_time:.4f} seconds\n")

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(array_sizes, serial_times, label='Serial', marker='o')
    plt.plot(array_sizes, threaded_times, label='Threading', marker='o')
    plt.plot(array_sizes, multiprocessing_times, label='Multiprocessing', marker='o')
    plt.xlabel('Array Size')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Performance Comparison of Serial, Threading, and Multiprocessing')
    plt.legend()
    plt.grid(True)

    # Save the plot as a PNG file
    plt.savefig('performance_comparison.png')
    
    plt.show()

    logging.info("Performance comparison completed. Insights can now be analyzed.")

if __name__ == '__main__':
    main()


# OBSERVATION:

# - **Function Complexity and Parallelism:**
#   - For functions with time complexity O(n):
#     - Directly using multiprocessing and multithreading is not suitable due to 
#       the overhead involved in communication between processes and threads, 
#       leading to poor performance. See `performance_comparison_for_On.png` for details.
  
#   - For functions with time complexity O(2^n):
#     - Multiprocessing performs better compared to both serialized and multithreading 
#       approaches. 
#       This indicates that for functions with exponential time complexity, 
#       parallel processing can significantly improve performance.

# - **Recommendation:**
#   - For programs with substantial execution time, 
#     consider using parallel processing to enhance efficiency.
#   - For less complex functions (e.g., linear time complexity), 
#     use parallel processing judiciously as it may not always 
#     yield performance benefits.
