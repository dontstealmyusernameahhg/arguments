def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial.__doc__)
print(factorial(5))
print(factorial(0))
print(factorial(1))
print(factorial(3))
print(factorial(10))
try:
    print(factorial(-5))  # This will raise an exception
except ValueError as e:
    print(e)