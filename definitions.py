properties_definitions = {
    "Parity": "The fact of being even or odd. ('The number's parity is even')",
    "Divisors": "A divisor is a number that divides into another without a remainder.",
    "Factors": "A factor of a number is a number that divides the given number evenly or exactly, leaving no remainder.",
    "Multiples": "Multiples are number you get when you multiple a certain number by an integer."
    
}

def get_property_names():
    return properties_definitions.keys()

def get_property_definition(property_name):
    return properties_definitions.get(property_name, "Definition not available.")


# Order to add (Based on Size/Relevance)

# fibonacci
# Prime
# Composite
# Square
# cube
# Perfect
# perfect square
# sublime
# triangular
# palindrome
# armstrong
# automorphic
# abundant
# deficient