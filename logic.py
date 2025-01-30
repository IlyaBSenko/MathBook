

def prime_checker(num):
    # check if num is greater than 1
    # check if it can only be divided evenly by 1 and itself (only has two factors)
    if num < 2:
        return False
    
    # check for factors from 2 -> square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: # make sure not divisible by anything other then num and 1
            return False
    
    return True


def composite_checker(num):
    if num > 1 and not prime_checker(num):
        return True
    return False


def perfect_number_checker(num):
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
    # check if its even or odd
    if num % 2 == 0:
        return "even"
    else:
        return "odd"