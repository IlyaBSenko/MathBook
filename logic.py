from gui import *

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
    if num < 0:
        return False
    fact = 1
    i = 1
    while fact < num:
        i += 1
        fact *= i
    return fact == num
    
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
    if num >= 1 and (num * (num + 1) / 2):
        return True if num.is_integer() else False
        
        

# WANT TO ADD:
# Multiples
# prime factors
# Perfect square root, display square root of a perfect squared 
# triangular checker
# palindrome checker
# armstrong number checker
