"""
properties_logic.py
-------------------
This module contains functions to determine various mathematical properties of numbers.
It includes functions for checking whether a number is prime, composite, perfect, a square,
a cube, part of the Fibonacci sequence, and more. It also provides functions for calculating
divisors, factorial, multiples, and additional properties. These functions are used by the
MathBook application to provide informative results about numbers.
"""

import math        # Import the math module for mathematical operations

def is_prime(num):
    """
    Checks if a number is prime.
    
    A prime number is a natural number greater than 1 that has no divisors other than 1 and itself.
    
    :param num: The number to check.
    :return: True if num is prime, False otherwise.
    """
    if num < 2:  # Numbers less than 2 are not prime
        return False
    
    # Test divisibility from 2 up to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If num is divisible by i, it is not prime
            return False
    
    return True  # No divisors found, num is prime

def is_composite(num):
    """
    Checks if a number is composite.
    
    A composite number is a positive integer that has at least one divisor other than 1 and itself.
    
    :param num: The number to check.
    :return: True if num is composite, False otherwise.
    """
    if num > 1 and not is_prime(num):  # If num is greater than 1 and not prime, it is composite
        return True
    
    return False  # Otherwise, num is not composite

def is_perfect(num):
    """
    Checks if a number is perfect.
    
    A perfect number is a positive number that is equal to the sum of its proper divisors.
    
    :param num: The number to check.
    :return: True if num is perfect, False otherwise.
    """
    if num <= 0:  # Perfect numbers must be positive
        return False

    divisor_sum = 1  # Start with 1, which is a divisor for any positive number

    # Loop through possible divisors from 2 up to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If i divides num evenly
            divisor_sum += i  # Add i to the sum of divisors
            if i != num // i:  # For non-square numbers, add the complementary divisor
                divisor_sum += num // i
    
    return divisor_sum == num  # True if the sum equals num

def parity_checker(num):
    """
    Determines whether a number is even or odd.
    
    :param num: The number to check.
    :return: "even" if num is even, "odd" if num is odd.
    """
    if num % 2 == 0:  # Check if num is divisible by 2
        return "even"
    else:
        return "odd"  # Otherwise, num is odd

def square_checker(num):
    """
    Checks if a number is a perfect square.
    
    :param num: The number to check.
    :return: True if num is a perfect square, False otherwise.
    """
    # A number is a perfect square if the square of its integer square root equals the number
    return num >= 0 and int(num ** 0.5) ** 2 == num

def cube_checker(num):
    """
    Checks if a number is a perfect cube.
    
    :param num: The number to check.
    :return: True if num is a perfect cube, False otherwise.
    """
    # Calculate the cube root, round it, and check if cubing the result returns num
    return round(num ** (1 / 3)) ** 3 == num

def get_divisors(num):
    """
    Computes all divisors of a given number.
    
    :param num: The number for which to find divisors.
    :return: A sorted list of divisors of num.
    """
    divisors = []  # Initialize an empty list for storing divisors
    
    # Loop from 1 up to the square root of the absolute value of num
    for i in range(1, int(abs(num) ** 0.5) + 1):
        if num % i == 0:  # If i divides num evenly
            divisors.append(i)  # Add i to the list
            if i != num // i:  # Avoid duplicates for perfect squares
                divisors.append(num // i)  # Add the complementary divisor
                
    return sorted(divisors)  # Return the divisors in sorted order

def compute_factorial(num):
    """
    Computes the factorial of a number if it is small enough.
    
    For numbers greater than 6, returns None because the factorial value may be too large.
    
    :param num: The number for which to compute the factorial.
    :return: The factorial of num, or None if num is too big.
    """
    if num <= 6:  # Only compute factorial for numbers <= 6
        if num < 0:  # Factorial is not defined for negative numbers
            return False
        
        if num == 1:  # The factorial of 1 is 1
            return 1
        
        fact = math.factorial(num)  # Compute the factorial using the math module
        return fact  # Return the computed factorial
    else:
        return None  # Indicate that the number is too big

def is_fibonacci(num):
    """
    Checks if a number is in the Fibonacci sequence.
    
    A number is Fibonacci if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    
    :param num: The number to check.
    :return: True if num is a Fibonacci number, False otherwise.
    """
    def is_perfect_square(n):
        # Check if n is a perfect square by comparing with the square of its integer square root
        return int(n ** 0.5) ** 2 == n

    # Return True if either expression results in a perfect square
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def is_sublime(num):
    """
    Checks if a number is sublime.
    
    A sublime number is one that has a perfect number of divisors and the sum of those divisors is also perfect.
    
    :param num: The number to check.
    :return: True if num is sublime, False otherwise.
    """
    if num <= 1:  # Numbers less than or equal to 1 cannot be sublime
        return False
    
    count = len(get_divisors(num))  # Count the number of divisors
    total = sum(get_divisors(num))   # Sum all the divisors
    
    # If both the count and the total are perfect numbers, num is considered sublime
    if is_perfect(count) and is_perfect(total):
        return True

def is_triangular(num):
    """
    Checks if a number is a triangular number.
    
    A triangular number can form an equilateral triangle.
    
    :param num: The number to check.
    :return: True if num is triangular, False otherwise.
    """
    if num < 0:  # Triangular numbers are non-negative
        return False

    # Solve the quadratic equation to determine if num is triangular
    x = (-1 + (1 + 8 * num) ** 0.5) / 2

    return x == int(x)  # If x is an integer, then num is triangular

def is_palindrome(num):
    """
    Checks if a number is palindromic.
    
    A palindromic number reads the same forwards and backwards.
    
    :param num: The number to check.
    :return: True if num is a palindrome, False otherwise.
    """
    if len(str(num)) < 2:  # Single-digit numbers are palindromic by definition
        return True

    # Convert num to a string and compare it with its reverse
    return str(num) == str(num)[::-1]

def is_armstrong(num):
    """
    Checks if a number is an Armstrong number.
    
    An Armstrong number is one that is equal to the sum of its own digits each raised to the power of 3.
    (Note: This implementation is tailored for three-digit numbers.)
    
    :param num: The number to check.
    :return: True if num is an Armstrong number, False otherwise.
    """
    true_num = num             # Store the original number
    str_num = str(num)         # Convert the number to a string to iterate over each digit
    num_as_list = []           # Initialize a list to hold each digit as a string

    # Add each digit from the string into the list
    for num in str_num:
        num_as_list.append(num)

    total = 0  # Initialize the total sum
    
    # Sum each digit raised to the power of 3
    for num in num_as_list:
        total += (int(num) ** 3)

    if total == true_num:  # If the sum equals the original number, it's an Armstrong number
        return True

def get_square_root(num):
    """
    Computes the square root of a number formatted to three decimal places.
    
    :param num: The number for which to compute the square root.
    :return: The square root as a string formatted to 3 decimal places, 0 if num is 0,
             or False if num is negative.
    """
    if num < 0:  # Square roots are not defined for negative numbers
        return False
    
    if num == 0:  # The square root of 0 is 0
        return 0
    
    # Compute the square root using math.sqrt and format it to three decimal places
    return f"{math.sqrt(num):.3f}"

def is_perfect_SR(num):
    """
    Checks if a number is a perfect square and returns its integer square root if it is.
    
    :param num: The number to check.
    :return: The integer square root if num is a perfect square, 0 if num is 0, or False otherwise.
    """
    if num < 0:  # Negative numbers cannot be perfect squares
        return False
    
    if num == 0:  # The perfect square root of 0 is 0
        return 0
        
    else:
        # Iterate through potential square roots to check if any square equals num
        for i in range(num):
            if i * i == num:
                return i  # Return the square root if found
            continue

def get_multiples(num):
    """
    Computes the first 5 multiples of a given number.
    
    :param num: The number for which to compute multiples.
    :return: A list containing the first 5 multiples of num, or a special message if num is 0.
    """
    if num == 0:  # Special case: 0 is a multiple of every number
        return "0 is a multiple of every number."
    
    multiples_list = [1, 2, 3, 4, 5]  # Multipliers for the first 5 multiples
    results = []  # Initialize a list to store the results
    
    # Compute each multiple by multiplying num with the multipliers
    for i in multiples_list:
        results.append(num * i)
    
    return results  # Return the list of multiples

def is_perfect_square(num):
    """
    Checks if a number is a perfect square.
    
    :param num: The number to check.
    :return: True if num is a perfect square, False otherwise.
    """
    if num < 0:  # Negative numbers cannot be perfect squares
        return False
    # Return True if the square of the integer square root equals num
    return int(num ** 0.5) ** 2 == num

def is_abundant(num):
    """
    Checks if a number is abundant.
    
    A number is abundant if the sum of its proper divisors is greater than the number itself.
    
    :param num: The number to check.
    :return: True if num is abundant, False otherwise.
    """
    if num <= 0:  # Abundant numbers are positive
        return False
    # Compute the sum of divisors (excluding num) and check if it is greater than num
    return sum(get_divisors(num)) - num > num

def is_deficient(num):
    """
    Checks if a number is deficient.
    
    A number is considered deficient if it is not abundant (i.e., the sum of its proper divisors is less than the number).
    
    :param num: The number to check.
    :return: True if num is deficient, False otherwise.
    """
    # Note: This simple definition may mark perfect numbers as deficient as well.
    if not is_abundant(num):
        return True

def is_automorphic(num):
    """
    Checks if a number is automorphic.
    
    A number is automorphic if its square ends with the same digits as the number itself.
    
    :param num: The number to check.
    :return: True if num is automorphic, False otherwise.
    """
    # Convert both num and its square to strings and check if the square ends with num
    return str(num ** 2).endswith(str(num))

# WANT TO ADD:
# prime factors
