from gui import *

properties_definitions = {
    "Integer": "A number that is not a fraction. (A whole number)",
    "Fraction": "A numerical quantity that is not a whole number.",
    "Rational": "A rational number is a number that can be expressed as the quotient/fraction of two integers.",
    "Parity": "The fact of being even or odd. ('The number's parity is even')",
    "Divisors": "A divisor is a number that divides into another without a remainder.",
    "Factors": "A factor of a number is a number that divides the given number evenly or exactly, leaving no remainder.",
    "Multiples": "Multiples are number you get when you multiple a certain number by an integer.",
    "Fibonacci Series": "A series of numbers in which each number (Fibonacci number) is the sum of the two preceding number.",
    "Prime numbers": "A number is prime if it can only be divided by itself and 1.",
    "Composite": "A composite number is a positive integer that has more than two factors. They are the opposite of prime numbers.",
    "Perfect": "A perfect number is a number that is equal to the sum of its factors other than the number itself.",
    "Perfect Square": "A perfect square is a number that can be expressed as the product of an integer by itself or as the second exponent of an integer.",
    "Sublime numbers": "A sublime number is a positive integer that has a perfect number of positive factors, and the sum of those factors is also a perfect number. For example, 12 is a sublime number because it has six positive factors (1, 2, 3, 4, 6, and 12), and the sum of those factors is 28, which is also a perfect number.",
    "Triangular Numbers": "A triangular number fits into this series of numbers (1, 3, 6, 10, 15, etc.) obtained by continued summation of the natural numbers 1, 2, 3, 4, 5, etc. Usually can be in the shape of a triangle.",
    "Palindromic number": "A number is palindromic if it remains the same when the digits are reversed.",
    "Armstrong number": "An Armstrong number is a number that is equal to the sum of its own digits, each raised to the power of the number of digits in that number; essentially, it's a number where the sum of its digits raised to their own place value equals the original number itself.",
    "Automorphic number": "An automorphic number is an integer whose square ends with the same digits as the original number. For example, 25 squared is 625, so 25 is an automorphic number.",
    "Abundant numbers": "In number theory, an abundant number is a positive integer where the sum of its proper divisors is greater than the number itself. The difference between the sum and the number is called the abundance.",
    "Deficient numbers": "A deficient number is a positive integer that is not a perfect or abundant number, and where the sum of its proper divisors is less than the number itself. They are essentially the opposite of abundant numbers."
    
    
}

def get_property_names():
    return properties_definitions.keys()

def get_property_definition(property_name):
    return properties_definitions.get(property_name, "Definition not available.")


# Order to add (Based on Size/Relevance)

# Square
# imaginary numbers
# real numbers