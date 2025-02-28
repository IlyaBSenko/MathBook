"""
properties_logic.py
-------------------
This module contains functions to determine various mathematical properties of numbers.
It includes functions for checking whether a number is prime, composite, perfect, a square,
a cube, part of the Fibonacci sequence, and more. It also provides functions for calculating
divisors, factorial, multiples, and additional properties.
"""

import math  

def is_prime(num):
    if num < 2:
        return False  

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  
            return False
    return True  

def is_composite(num):
    return num > 1 and not is_prime(num)

def is_perfect(num):
    if num <= 0:
        return False  

    divisor_sum = 1 
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  
            divisor_sum += i 
            if i != num // i:  
                divisor_sum += num // i  
    return divisor_sum == num  

def parity_checker(num):
    return "even" if num % 2 == 0 else "odd"

def square_checker(num):
    return num >= 0 and int(num ** 0.5) ** 2 == num

def cube_checker(num):
    return round(num ** (1 / 3)) ** 3 == num

def get_divisors(num):
    divisors = []  
    for i in range(1, int(abs(num) ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)  
            if i != num // i:
                divisors.append(num // i)  
    return sorted(divisors) 

def compute_factorial(num):
    if num < 0:
        return False  
    if num <= 6:
        return math.factorial(num)  
    return None  

def is_fibonacci(num):
    def is_perfect_square(n):
        return int(n ** 0.5) ** 2 == n

    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def is_sublime(num):
    if num <= 1:
        return False  
    count = len(get_divisors(num))  
    total = sum(get_divisors(num))   
    return is_perfect(count) and is_perfect(total)

def is_triangular(num):
    if num < 0:
        return False 
    x = (-1 + (1 + 8 * num) ** 0.5) / 2
    return x == int(x)  

# help from thomas
def is_palindrome(num):
    s = str(num)  
    return s == s[::-1]  

def is_armstrong(num):
    digits = str(num)  
    power = len(digits)  
    total = sum(int(digit) ** power for digit in digits)  
    return total == num  

def get_square_root(num):
    if num < 0:
        return False  
    if num == 0:
        return 0  
    return f"{math.sqrt(num):.3f}"  

def get_perfect_square_root(num):
    if num < 0:
        return False  
    if num == 0:
        return 0 
    for i in range(num + 1):
        if i * i == num:
            return i  

def get_multiples(num):
    if num == 0:
        return []  
   
    return [num * i for i in [1, 2, 3, 4, 5]]

def is_perfect_square(num):
    if num < 0:
        return False  
    return int(num ** 0.5) ** 2 == num  

def is_abundant(num):
    if num <= 0:
        return False 
    return sum(get_divisors(num)) - num > num

def is_deficient(num):
    return (sum(get_divisors(num)) - num) < num

def is_automorphic(num):
    return str(num ** 2).endswith(str(num))
