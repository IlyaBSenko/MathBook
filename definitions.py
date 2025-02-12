"""
definitions.py
--------------
This module provides definitions for various mathematical terms and properties.
It contains a dictionary mapping property names to their detailed definitions and functions
to retrieve the names and definitions. These definitions are used in the MathBook application
to educate users about different mathematical concepts.
"""

# Dictionary mapping mathematical property names to their definitions.
properties_definitions = {
    "Integer": "A number that is not a fraction. (A whole number)",
    "Fraction": "A numerical quantity that is not a whole number.",
    "Rational": "A rational number is a number that can be expressed as the quotient/fraction of two integers.",
    "Parity": "The fact of being even or odd. ('The number's parity is even')",
    "Divisors": "A divisor is a number that divides into another without a remainder.",
    "Factors": "A factor of a number is a number that divides the given number evenly or exactly, leaving no remainder.",
    "Multiples": "Multiples are numbers you get when you multiply a certain number by an integer.",
    "Fibonacci Series": "A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers.",
    "Prime numbers": "A number is prime if it can only be divided by itself and 1.",
    "Composite": "A composite number is a positive integer that has more than two factors. They are the opposite of prime numbers.",
    "Imaginary numbers": "A number that is expressed in terms of the square root of a negative number (usually the square root of −1, represented by i or j).",
    "Perfect": "A perfect number is a number that is equal to the sum of its factors other than the number itself.",
    "Perfect Square": "A perfect square is a number that can be expressed as the product of an integer by itself or as the second exponent of an integer.",
    "Sublime numbers": ("A sublime number is a positive integer that has a perfect number of positive factors, and the sum "
                        "of those factors is also a perfect number. For example, 12 is sublime because it has six positive "
                        "factors (1, 2, 3, 4, 6, and 12), and the sum of those factors is 28, which is also a perfect number."),
    "Triangular Numbers": ("A triangular number fits into a series (1, 3, 6, 10, 15, etc.) obtained by the continued "
                           "summation of natural numbers. They can be visually represented in the shape of a triangle."),
    "Palindromic number": "A number is palindromic if it remains the same when its digits are reversed.",
    "Armstrong number": ("An Armstrong number is a number that is equal to the sum of its own digits, each raised to the "
                         "power of the number of digits in that number."),
    "Automorphic number": ("An automorphic number is an integer whose square ends with the same digits as the number itself. "
                           "For example, 25 squared is 625, so 25 is automorphic."),
    "Abundant numbers": ("A positive integer is abundant if the sum of its proper divisors is greater than the number itself. "
                         "The difference is known as the abundance."),
    "Deficient numbers": ("A deficient number is a positive integer for which the sum of its proper divisors is less than the "
                          "number itself. They are essentially the opposite of abundant numbers.")
}

def get_property_names():
    """
    Retrieves all property names for which definitions are available.
    
    :return: An iterable of the property names (dictionary keys).
    """
    return properties_definitions.keys()

def get_property_definition(property_name):
    """
    Retrieves the definition for a specified property.
    
    :param property_name: The name of the property.
    :return: The definition string if available; otherwise, a default message.
    """
    return properties_definitions.get(property_name, "Definition not available.")
