# Optimized function to perform a CPU-intensive computation (Fibonacci calculation)
# Function BigO: O(n)
def compute1(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Function to perform a CPU-intensive computation (Fibonacci calculation)
# Function BigO: O(2^n)
def compute2(n):
    if n <= 1:
        return n
    else:
        return compute2(n-1) + compute2(n-2)
    
print(compute1(10))
print(compute2(10))