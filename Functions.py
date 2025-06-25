#functions in pyton
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
def subtract(a, b):                             
    """Returns the difference of a and b."""
    return a - b
def multiply(a, b):
    """Returns the product of a and b."""
    return a * b
def divide(a, b):
    """Returns the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(base, exponent):                  
    """Returns base raised to the power of exponent."""
    return base ** exponent
def factorial(n):
    """Returns the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a)
def lcm(a, b):
    """Returns the least common multiple of a and b."""
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined for zero.")
    return abs(a * b) // gcd(a, b)
def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    '#arguments'
def is_palindrome(s):
    """Returns True if s is a palindrome, otherwise False."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]