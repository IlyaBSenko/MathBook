from gui import *
import math

def is_prime(num):
    # check if num is greater than 1
    # check if it can only be divided evenly by 1 and itself (only has two factors)
    if num < 2:
        return False
    
    # check for factors from 2 -> square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: # make sure not divisible by anything other then num and 1
            return False
    
    return True


def is_composite(num):
    if num > 1 and not is_prime(num):
        return True
    return False


def is_perfect(num):
    # add up all of its positive divisors, excluding the number itself, and see if the sum equals the original number
    if num <= 0:
        return False

    # Find the sum of proper divisors (excluding the number itself)
    divisor_sum = 1  # 1 is a divisor for all positive numbers

    # Loop to find divisors up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            # Add the corresponding divisor (num // i)
            if i != num // i:
                divisor_sum += num // i

    # Check if the sum of divisors equals the number
    return divisor_sum == num

def parity_checker(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# A number is a square number if it can be expressed as the square of an integer
def square_checker(num):
    return num >= 0 and int(num ** 0.5) ** 2 == num

# A number is a cube number if it can be expressed as the cube of an integer
def cube_checker(num):
    return  round(num ** (1 / 3)) ** 3 == num

# Show all positive divisors of a number
def get_divisors(num):
    if num == 0:
        return []
    divisors = []
    for i in range(1, int(abs(num) ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sorted(divisors)

# Check if a number is a factorial of some integer
def is_factorial(num):
    # multiply num by every pos int below it, all the way down to 1
    if num <= 6:
        if num < 0:
            return False
        if num == 1:
            return 1
        fact = math.factorial(num)
        return fact
    else:
        return None
    
# A number is part of the Fibonacci sequence if one of these two conditions is true:
# 5 * num^2 + 4 or 5 * num^2 - 4 is a perfect square
def is_fibonacci(num):
    def is_perfect_square(n):
        return int(n ** 0.5) ** 2 == n

    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


def is_sublime(num):
    # count the total number of divisors of n
    # store that total number in a variable (total)
    # sum the divisors
    # store the result in a variable
    # check whether the total and sum are perfect numbers are not
    # if they are, num is a sublime number
    if num <= 1:
        return False
    
    count = len(get_divisors(num))
    total = sum(get_divisors(num))
    if is_perfect(count) and is_perfect(total):
        return True
    
def is_triangular(num):
    if num < 0:
        return False

    x = (-1 + (1 + 8 * num) ** 0.5) / 2

    return x == int(x)

# with help from thomas for crazy python trick
def is_palindrome(num):
    if len(str(num)) < 2:
        return True

    return str(num) == str(num)[::-1]


def is_armstrong(num):
    true_num = num
    str_num = str(num)
    num_as_list = []

    for num in str_num:
        num_as_list.append(num)

    total = 0
    for num in num_as_list:
        total += (int(num) ** 3)

    if total == true_num:
        return True
    
def get_square_root(num):
    if num < 0:
        return False
    
    if num == 0:
        return 0
    
    return f"{math.sqrt(num):.3f}"
    
def is_perfect_SR(num):
    if num < 0:
        return False
    
    if num == 0:
        return 0
        
    else:
        for i in range(num):
            if i * i == num:
                return i
            continue
        
def get_multiples(num):
    if num == 0:
        return "0 is a multiple of every number."
    
    multiples_list = [1, 2, 3, 4, 5]
    results = []
    
    for i in multiples_list:
        results.append(num * i)
    
    return results
        


# WANT TO ADD:
# Multiples
# prime factors
