import tkinter as tk
from properties_logic import *

# Function to handle a button click
def button_click(event=None, result_label=None):       
    try:
            
        user_inp = event.widget.get().strip()
        num = int(user_inp)

        # Call logic functions and get results
        prime = is_prime(num)
        parity = parity_checker(num)
        perfect = is_perfect(num)
        composite = is_composite(num)
        square = square_checker(num)
        cube = cube_checker(num)
        divisors = get_divisors(num)
        factorial = is_factorial(num)
        fibonacci = is_fibonacci(num)
        sublime = is_sublime(num)
        triangular = is_triangular(num)
        palindrome = is_palindrome(num)
        armstrong = is_armstrong(num)
        perfect_square_root = is_perfect_SR(num)
        square_root = get_square_root(num)
        multiples = get_multiples(num)


        # Format results
        results = []
        results.append(f"{num} is {parity}.")

        if num < 0:
            results.append(f"{num} is negative and does not have properties like prime, composite, or multiples.")
            
        if num == 0:
            results.append(f"{num} is a multiple of every number.")
            results.append("Every non-zero number is considered a divisor of {num}.")
        else:
            results.append(f"The first 5 multiples of {num} are {multiples}.")
            results.append(f"Divisors: {divisors}")
            
        if num <= 0:
            results.append(f"{num} is neither prime nor composite.")
            results.append(f"{num} is a palindrome.")
            results.append(f"{num} is an armstrong number.")
            
        if not perfect_square_root:
            results.append(f"The square root of {num} is {square_root}")
            
        property_checks = [
            (prime, f"{num} is prime."),
            (composite, f"{num} is composite."),
            (perfect, f"{num} is perfect."),
            (square, f"{num} is a square number."),
            (cube, f"{num} is a cube number."),
            (fibonacci, f"{num} is a Fibonacci number."),
            (sublime, f"{num} is sublime."),
            (triangular, f"{num} is triangular."),
            (palindrome, f"{num} is a palindrome."),
            (armstrong, f"{num} is an armstrong number."),
        ]

        for condition, message in property_checks:
            if condition:
                results.append(message)
        if perfect_square_root:
            results.append(f"The square root of {num} is {perfect_square_root}")
        
        if factorial == None:
            results.append(f"Number too big to check for factorial!")
        else:
            results.append(f"The factorial of {num} is ({factorial}!)")
        # Update the result label
        result_label.config(text="\n".join(results))

    except ValueError:
        result_label.config(text="Please enter a valid number.")
            
def show_search_entry_prop():
    create_search_window("Properties", button_click)
    
def show_search_entry_trivia():
    create_search_window("Trivia", button_click)
    
def show_search_entry_lore():
    create_search_window("Lore", button_click)
    
# for real world applications
def show_search_entry_RW():
    create_search_window("Real World Applications", button_click)
    
def create_search_window(title, button_click_callback):
    # Create a new window
    topLevel = tk.Toplevel()
    topLevel.title(title)

    # Add a search entry and result label
    searchEntry = tk.Entry(topLevel)
    searchEntry.pack()

    result_label = tk.Label(topLevel, text="", bg="lightgray", fg="black", width=50, height=10, anchor="nw")
    result_label.pack(pady=10)

    # Bind Enter key to trigger the callback
    searchEntry.bind("<Return>", lambda event: button_click_callback(event, result_label))

    return topLevel

    
# Main window setup
window = tk.Tk()
window.title("MathBook")

# Label widgets
label1 = tk.Label(window, text="Hello! Welcome to MathBook!")
label1.pack()

label2 = tk.Label(window, text="Click what you would like to learn!")
label2.pack()

# Button widget
button1 = tk.Button(window, text="Properties", command=show_search_entry_prop)
button2 = tk.Button(window, text="Trivia", command=show_search_entry_trivia)
button3 = tk.Button(window, text="Lore", command=show_search_entry_lore)
button4 = tk.Button(window, text="Real World Applications", command=show_search_entry_RW)
button1.pack()
button2.pack()
button3.pack()
button4.pack()
