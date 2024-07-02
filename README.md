# MultiThreading vs MultiProcessing in Python

I have written a simple cpu intensive recursive calculation that aims to compute Fibonacci numbers recursively. 
Ths script has the same task done serially, then using the brilliant concurrent.futures doing multithreading and multiprocessing.

This script is written to highlight that for CPU Intensive tasks SPECIFICALLY in Python, multiprocessing can be more beneficial in due to the GIL (Global Interpreter Lock), which only lets one thread execute Python bytecode at a time. But in Multi processing, since there are multiple proccesses/instances of the Python instance running separately, each with its own memory space (and not shared like in multi threading), these processes can execute the code truly parallelly (and not concurrently like in Multi Threading). 
Concurrenlty just meanas that it can handle to do multiple tasks, but just not at the same time simultaneously. Instead, it might quickly switch between them.

Multithreading in Python only makes sense when you plan to do a lot of I/O based tasks (e.g. making API calls, writing to disk etc). Multiprocessing in Python only works for CPU intensive tasks. 

