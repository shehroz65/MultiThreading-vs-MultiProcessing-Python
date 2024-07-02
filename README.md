# CPU Intensive Task: MultiThreading vs MultiProcessing in Python

A CPU intensive calculation script that computes Fibonacci numbers recursively. 
Ths script has the same task done serially, then using the **concurrent.futures** library doing multithreading and multiprocessing.

# Key Concepts:

**Global Interpreter Lock (GIL)**: A mechanism in Python that prevents multiple threads from executing python bytecode at the same time.
**Concurrency**: Handling multiple tasks and switching quickly between them instead of processing them simultaneously. 
**Parallelism**: Executing multiple tasks at the same time parallelly. Involves more cores. 

**Why Multi Processing?**
In Python, for truly parallel needed executions (like cpu intensive calculations divided among cores), parallelism is needed. And multiprocessing is beneficial here because the cores can't afford to wait.
However, there is greater communication overhead so some exerimentation is necessary to decide the ideal amount of cores for your use case. Also, more system resources may be needed. 

**Why Multi Threading**: 
For concurrent tasks where the executor can afford to wait like I/O operations, network requests, file reads/writes etc, muli threading can be useful. It has less communication overhead, uses less resources and is less intensive. 
