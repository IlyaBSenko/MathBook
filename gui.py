import tkinter as tk
from logic import *

# Function to handle a button click
def button_click(event=None):  # Accept the event parameter for key bindings
    try:
        user_inp = searchEntry.get().strip()
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

        # Format results
        results = []
        results.append(f"{num} is {parity}.")
        # results.append(f"The square root of {num} is {squareRoot}.")

        if num < 0:
            results.append(f"{num} is negative.")
            
        if num <= 0:
            results.append(f"{num} is neither prime nor composite.")
            results.append(f"{num} is a palindrome.")
            results.append(f"{num} is an armstrong number.")
            
        if not perfect_square_root:
            results.append(f"The square root of {num} is {square_root}")
            
        else:
            if prime:
                results.append(f"{num} is prime.")
            if composite:
                results.append(f"{num} is composite.")
            if perfect:
                results.append(f"{num} is perfect.")
            if square:
                results.append(f"{num} is a square number.")
            if cube:
                results.append(f"{num} is a cube number.")
            if divisors:
                results.append(f"Divisors: {divisors}")
            if fibonacci:
                results.append(f"{num} is a Fibonacci Number.")
            if sublime:
                results.append(f"{num} is sublime.")
            if triangular:
                results.append(f"{num} is triangular.")
            if palindrome:
                results.append(f"{num} is a palindrome.")
            if armstrong:
                results.append(f"{num} is an armstrong number.")
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

# Main window setup
window = tk.Tk()
window.title("MathBook")

# Label widgets
label1 = tk.Label(window, text="Hello! Welcome to MathBook!")
label1.pack()

label2 = tk.Label(window, text="Search a number!")
label2.pack()

# Entry widget
searchEntry = tk.Entry(window)
searchEntry.pack()

# Bind the Enter key to trigger the button click function
searchEntry.bind("<Return>", button_click)

# Button widget
button1 = tk.Button(window, text="Enter", command=button_click)
button1.pack()

# Label to display results
result_label = tk.Label(window, text="", bg="lightgray", width=50, height=10, anchor="nw")
result_label.pack(pady=10)


