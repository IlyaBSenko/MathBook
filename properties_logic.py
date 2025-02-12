from gui import *
import math


def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: 
            return False
    
    return True


def is_composite(num):
    if num > 1 and not is_prime(num):
        return True
    
    return False


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
    if num % 2 == 0:
        return "even"
    
    else:
        return "odd"

def square_checker(num):
    return num >= 0 and int(num ** 0.5) ** 2 == num

def cube_checker(num):
    return  round(num ** (1 / 3)) ** 3 == num

def get_divisors(num):
    divisors = []
    
    for i in range(1, int(abs(num) ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
                
    return sorted(divisors)

def is_factorial(num):
    if num <= 6:
        if num < 0:
            return False
        
        if num == 1:
            return 1
        
        fact = math.factorial(num)
        return fact
   
    else:
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
    
    if is_perfect(count) and is_perfect(total):
        return True
    
def is_triangular(num):
    if num < 0:
        return False

    x = (-1 + (1 + 8 * num) ** 0.5) / 2

    return x == int(x)

def is_palindrome(num):
    if len(str(num)) < 2:
        return True

    # help from thomas
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

def is_perfect_square(num):
    if num < 0:
        return False
    return int(num ** 0.5) ** 2 == num

def is_abundant(num):
    if num <= 0:
        return False
    return sum(get_divisors(num)) - num > num

def is_deficient(num):
    if not is_abundant(num):
        return True

def is_automorphic(num):
    return str(num ** 2).endswith(str(num))


# WANT TO ADD:
# prime factors
