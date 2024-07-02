# CPU Intensive Task: MultiThreading vs MultiProcessing in Python

I have written a simple cpu intensive recursive calculation that aims to compute Fibonacci numbers recursively. 
Ths script has the same task done serially, then using the brilliant concurrent.futures doing multithreading and multiprocessing.

# Key Concepts:

**Global Interpreter Lock (GIL)**: A mechanism in Python that prevents multiple threads from executing python bytecode at the same time.
**Concurrency**: Handling multiple tasks and switching quickly between them instead of processing them simultaneously. 
**Parallelism**: Executing multiple tasks at the same time parallelly. Involves more cores. 

This script is written to highlight that for **CPU Intensive tasks SPECIFICALLY in Python**, multiprocessing can be more beneficial due to the GIL (Global Interpreter Lock).
Multithreading in Python only makes sense when you plan to do a lot of I/O based tasks (e.g. making API calls, writing to disk etc). Multiprocessing in Python only works for CPU intensive tasks. 

