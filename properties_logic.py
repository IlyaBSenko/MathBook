"""
properties_logic.py
-------------------
This module contains functions to determine various mathematical properties of numbers.
It includes functions for checking whether a number is prime, composite, perfect, a square,
a cube, part of the Fibonacci sequence, and more. It also provides functions for calculating
divisors, factorial, multiples, and additional properties. These functions are used by the
MathBook application to provide informative results about numbers.
"""

import math  # Import the math module for mathematical operations

def is_prime(num):
    """
    Checks if a number is prime.
    
    A prime number is a natural number greater than 1 that has no divisors other than 1 and itself.
    
    :param num: The number to check.
    :return: True if num is prime, False otherwise.
    """
    if num < 2:
        return False  # Numbers less than 2 are not prime
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Found a divisor; therefore, not prime
    
    return True  # No divisors found; num is prime

def is_composite(num):
    """
    Checks if a number is composite.
    
    A composite number is a positive integer that has at least one divisor other than 1 and itself.
    
    :param num: The number to check.
    :return: True if num is composite, False otherwise.
    """
    return num > 1 and not is_prime(num)

def is_perfect(num):
    """
    Checks if a number is perfect.
    
    A perfect number is a positive number equal to the sum of its proper divisors.
    
    :param num: The number to check.
    :return: True if num is perfect, False otherwise.
    """
    if num <= 0:
        return False

    divisor_sum = 1  # Start with 1 (always a divisor)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i
    
    return divisor_sum == num

def parity_checker(num):
    """
    Determines whether a number is even or odd.
    
    :param num: The number to check.
    :return: "even" if num is even, "odd" otherwise.
    """
    return "even" if num % 2 == 0 else "odd"

def square_checker(num):
    """
    Checks if a number is a perfect square.
    
    :param num: The number to check.
    :return: True if num is a perfect square, False otherwise.
    """
    return num >= 0 and int(num ** 0.5) ** 2 == num

def cube_checker(num):
    """
    Checks if a number is a perfect cube.
    
    :param num: The number to check.
    :return: True if num is a perfect cube, False otherwise.
    """
    return round(num ** (1 / 3)) ** 3 == num

def get_divisors(num):
    """
    Computes all divisors of a given number.
    
    :param num: The number for which to find divisors.
    :return: A sorted list of divisors of num.
    """
    divisors = []
    for i in range(1, int(abs(num) ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sorted(divisors)

def compute_factorial(num):
    """
    Computes the factorial of a number if it is small enough.
    
    For numbers greater than 6, returns None because the factorial value may be too large.
    
    :param num: The number for which to compute the factorial.
    :return: The factorial of num, or None if num is too big.
    """
    if num < 0:
        return False  # Factorial not defined for negative numbers
    if num <= 6:
        return math.factorial(num)
    return None

def is_fibonacci(num):
    """
    Checks if a number is in the Fibonacci sequence.
    
    A number is Fibonacci if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    
    :param num: The number to check.
    :return: True if num is Fibonacci, False otherwise.
    """
    def is_perfect_square(n):
        return int(n ** 0.5) ** 2 == n

    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def is_sublime(num):
    """
    Checks if a number is sublime.
    
    A sublime number has both a perfect number of divisors and a perfect sum of those divisors.
    
    :param num: The number to check.
    :return: True if num is sublime, False otherwise.
    """
    if num <= 1:
        return False
    count = len(get_divisors(num))
    total = sum(get_divisors(num))
    return is_perfect(count) and is_perfect(total)

def is_triangular(num):
    """
    Checks if a number is triangular.
    
    A triangular number can form an equilateral triangle.
    
    :param num: The number to check.
    :return: True if num is triangular, False otherwise.
    """
    if num < 0:
        return False
    # Solve the quadratic equation n(n+1)/2 = num
    x = (-1 + (1 + 8 * num) ** 0.5) / 2
    return x == int(x)

def is_palindrome(num):
    """
    Checks if a number is palindromic.
    
    :param num: The number to check.
    :return: True if num is a palindrome, False otherwise.
    """
    s = str(num)
    return s == s[::-1]

def is_armstrong(num):
    """
    Checks if a number is an Armstrong number.
    
    An Armstrong number equals the sum of its digits each raised to the power of the number of digits.
    
    :param num: The number to check.
    :return: True if num is Armstrong, False otherwise.
    """
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

def get_square_root(num):
    """
    Computes the square root of a number formatted to three decimal places.
    
    :param num: The number for which to compute the square root.
    :return: The square root as a string formatted to 3 decimal places, 0 if num is 0,
             or False if num is negative.
    """
    if num < 0:
        return False
    if num == 0:
        return 0
    return f"{math.sqrt(num):.3f}"

def get_perfect_square_root(num):
    """
    If a number is a perfect square, returns its integer square root.
    
    :param num: The number to check.
    :return: The integer square root if num is a perfect square, 0 if num is 0,
             or False if num is negative.
    """
    if num < 0:
        return False
    if num == 0:
        return 0
    for i in range(num + 1):
        if i * i == num:
            return i

def get_multiples(num):
    """
    Computes the first 5 multiples of a given number.
    
    :param num: The number for which to compute multiples.
    :return: A list containing the first 5 multiples of num. Returns an empty list for 0.
    """
    if num == 0:
        return []
    return [num * i for i in [1, 2, 3, 4, 5]]

def is_perfect_square(num):
    """
    Checks if a number is a perfect square.
    
    :param num: The number to check.
    :return: True if num is a perfect square, False otherwise.
    """
    if num < 0:
        return False
    return int(num ** 0.5) ** 2 == num

def is_abundant(num):
    """
    Checks if a number is abundant.
    
    A number is abundant if the sum of its proper divisors is greater than the number.
    
    :param num: The number to check.
    :return: True if num is abundant, False otherwise.
    """
    if num <= 0:
        return False
    return sum(get_divisors(num)) - num > num

def is_deficient(num):
    """
    Checks if a number is deficient.
    
    A number is deficient if the sum of its proper divisors is less than the number.
    (Note: This definition may classify perfect numbers as deficient.)
    
    :param num: The number to check.
    :return: True if num is deficient, False otherwise.
    """
    # Using a more explicit check:
    return (sum(get_divisors(num)) - num) < num

def is_automorphic(num):
    """
    Checks if a number is automorphic.
    
    A number is automorphic if its square ends with the same digits as the number.
    
    :param num: The number to check.
    :return: True if num is automorphic, False otherwise.
    """
    return str(num ** 2).endswith(str(num))
