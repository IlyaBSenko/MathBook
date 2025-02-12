"""
properties_logic.py
-------------------
This module contains functions to determine various mathematical properties of numbers.
It includes functions for checking whether a number is prime, composite, perfect, a square,
a cube, part of the Fibonacci sequence, and more. It also provides functions for calculating
divisors, factorial, multiples, and additional properties.
"""

import math  # Import math to use math functions like sqrt and factorial

def is_prime(num):
    """
    Checks if a number is prime.
    
    :param num: The number to check.
    :return: True if num is prime, False otherwise.
    """
    if num < 2:
        return False  # Numbers less than 2 are not prime

    # Loop from 2 to the integer square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If num is divisible by i, it is not prime
            return False
    return True  # If no divisors were found, num is prime

def is_composite(num):
    """
    Checks if a number is composite.
    
    :param num: The number to check.
    :return: True if num is composite, False otherwise.
    """
    # A number is composite if it is greater than 1 and not prime
    return num > 1 and not is_prime(num)

def is_perfect(num):
    """
    Checks if a number is perfect.
    
    :param num: The number to check.
    :return: True if num is perfect, False otherwise.
    """
    if num <= 0:
        return False  # Perfect numbers must be positive

    divisor_sum = 1  # Start with 1, which is always a divisor
    # Loop from 2 to sqrt(num) to find divisors
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If i divides num evenly
            divisor_sum += i  # Add i to the sum
            if i != num // i:  # If i is not the square root of num
                divisor_sum += num // i  # Add the complementary divisor
    return divisor_sum == num  # Return True if the sum equals num

def parity_checker(num):
    """
    Determines whether a number is even or odd.
    
    :param num: The number to check.
    :return: "even" if num is even, "odd" otherwise.
    """
    # Return "even" if divisible by 2, otherwise "odd"
    return "even" if num % 2 == 0 else "odd"

def square_checker(num):
    """
    Checks if a number is a perfect square.
    
    :param num: The number to check.
    :return: True if num is a perfect square, False otherwise.
    """
    # Ensure the number is non-negative and compare the square of the integer square root to num.
    return num >= 0 and int(num ** 0.5) ** 2 == num

def cube_checker(num):
    """
    Checks if a number is a perfect cube.
    
    :param num: The number to check.
    :return: True if num is a perfect cube, False otherwise.
    """
    # Compute cube root, round it and then cube it; check if it equals num.
    return round(num ** (1 / 3)) ** 3 == num

def get_divisors(num):
    """
    Computes all divisors of a given number.
    
    :param num: The number to check.
    :return: A sorted list of divisors of num.
    """
    divisors = []  # List to hold divisors
    # Loop from 1 to the square root of the absolute value of num
    for i in range(1, int(abs(num) ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)  # Add the divisor
            if i != num // i:
                divisors.append(num // i)  # Add the complementary divisor if not a duplicate
    return sorted(divisors)  # Return sorted list for readability

def compute_factorial(num):
    """
    Computes the factorial of a number if it is small enough.
    
    :param num: The number to compute the factorial for.
    :return: The factorial of num, or None if num is greater than 6.
    """
    if num < 0:
        return False  # Factorial is not defined for negative numbers
    if num <= 6:
        return math.factorial(num)  # Compute factorial using math.factorial
    return None  # For larger numbers, return None

def is_fibonacci(num):
    """
    Checks if a number is in the Fibonacci sequence.
    
    :param num: The number to check.
    :return: True if num is Fibonacci, False otherwise.
    """
    def is_perfect_square(n):
        # Check if n is a perfect square
        return int(n ** 0.5) ** 2 == n

    # Check if one of the expressions yields a perfect square
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def is_sublime(num):
    """
    Checks if a number is sublime.
    
    :param num: The number to check.
    :return: True if num is sublime, False otherwise.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 cannot be sublime
    count = len(get_divisors(num))  # Count of divisors
    total = sum(get_divisors(num))   # Sum of divisors
    # Return True only if both the count and the total are perfect numbers
    return is_perfect(count) and is_perfect(total)

def is_triangular(num):
    """
    Checks if a number is triangular.
    
    :param num: The number to check.
    :return: True if num is triangular, False otherwise.
    """
    if num < 0:
        return False  # Triangular numbers are non-negative
    # Solve the quadratic equation n(n+1)/2 = num for n
    x = (-1 + (1 + 8 * num) ** 0.5) / 2
    return x == int(x)  # If x is an integer, num is triangular

def is_palindrome(num):
    """
    Checks if a number is palindromic.
    
    :param num: The number to check.
    :return: True if num is a palindrome, False otherwise.
    """
    s = str(num)  # Convert the number to a string
    return s == s[::-1]  # Check if the string is the same when reversed

def is_armstrong(num):
    """
    Checks if a number is an Armstrong number.
    
    :param num: The number to check.
    :return: True if num is Armstrong, False otherwise.
    """
    digits = str(num)  # Convert number to string to iterate over digits
    power = len(digits)  # The number of digits
    total = sum(int(digit) ** power for digit in digits)  # Sum each digit raised to the power
    return total == num  # Return True if the total equals the original number

def get_square_root(num):
    """
    Computes the square root of a number formatted to three decimal places.
    
    :param num: The number to compute the square root for.
    :return: The square root as a string (3 decimals), 0 if num is 0, or False if negative.
    """
    if num < 0:
        return False  # Negative numbers do not have a real square root
    if num == 0:
        return 0  # The square root of 0 is 0
    return f"{math.sqrt(num):.3f}"  # Format the square root to 3 decimal places

def get_perfect_square_root(num):
    """
    If a number is a perfect square, returns its integer square root.
    
    :param num: The number to check.
    :return: The integer square root if num is a perfect square; 0 for 0; False if negative.
    """
    if num < 0:
        return False  # Negative numbers cannot be perfect squares
    if num == 0:
        return 0  # The square root of 0 is 0
    # Iterate through all numbers from 0 up to num to find the square root
    for i in range(num + 1):
        if i * i == num:
            return i  # Found the integer square root

def get_multiples(num):
    """
    Computes the first 5 multiples of a given number.
    
    :param num: The number to compute multiples for.
    :return: A list of the first 5 multiples; an empty list for 0.
    """
    if num == 0:
        return []  # Return an empty list for 0
    # Use list comprehension to multiply num by each number in the list
    return [num * i for i in [1, 2, 3, 4, 5]]

def is_perfect_square(num):
    """
    Checks if a number is a perfect square.
    
    :param num: The number to check.
    :return: True if num is a perfect square, False otherwise.
    """
    if num < 0:
        return False  # Negative numbers cannot be perfect squares
    return int(num ** 0.5) ** 2 == num  # Compare square of the integer square root to num

def is_abundant(num):
    """
    Checks if a number is abundant.
    
    :param num: The number to check.
    :return: True if num is abundant, False otherwise.
    """
    if num <= 0:
        return False  # Abundant numbers are positive
    # Check if the sum of proper divisors (excluding the number itself) is greater than num
    return sum(get_divisors(num)) - num > num

def is_deficient(num):
    """
    Checks if a number is deficient.
    
    :param num: The number to check.
    :return: True if num is deficient, False otherwise.
    """
    # A number is deficient if the sum of its proper divisors is less than the number
    return (sum(get_divisors(num)) - num) < num

def is_automorphic(num):
    """
    Checks if a number is automorphic.
    
    :param num: The number to check.
    :return: True if num is automorphic, False otherwise.
    """
    # Check if the square of num (as a string) ends with num (as a string)
    return str(num ** 2).endswith(str(num))
