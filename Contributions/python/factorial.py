def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Example usage
num = 5
print(f"The factorial of {num} is {factorial(num)}")
