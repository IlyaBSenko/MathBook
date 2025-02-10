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
    "Perfect Square": "A perfect square is a number that can be expressed as the product of an integer by itself or as the second exponent of an integer."
    
    
}

def get_property_names():
    return properties_definitions.keys()

def get_property_definition(property_name):
    return properties_definitions.get(property_name, "Definition not available.")


# Order to add (Based on Size/Relevance)

# Square
# sublime
# triangular
# palindrome
# armstrong
# automorphic
# abundant
# deficient