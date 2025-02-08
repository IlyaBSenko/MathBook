properties_definitions = {
    "Automorphic": "An automorphic number is a number whose square ends with the number itself.",
    "Perfect Square": "A perfect square is a number that can be expressed as the square of an integer.",
    "Prime Number": "A prime number is a number greater than 1 that has no divisors other than 1 and itself.",
    "Abundant Number": "An abundant number is a number whose sum of proper divisors exceeds the number itself.",
    "Armstrong Number": "An Armstrong number (or narcissistic number) is a number equal to the sum of its digits each raised to the power of the number of digits."
    # Add more definitions here
}

def get_property_names():
    return properties_definitions.keys()

def get_property_definition(property_name):
    return properties_definitions.get(property_name, "Definition not available.")