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

        # Format results
        results = []
        results.append(f"{num} is {parity}.")

        if num < 0:
            results.append(f"{num} is negative.")
        if num <= 0:
            results.append(f"{num} is neither prime nor composite.")
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
            if factorial:
                results.append(f"{num} is a factorial of ({factorial}!)")
            if fibonacci:
                results.append(f"{num} is a Fibonacci Number.")
            if sublime:
                results.append(f"{num} is sublime.")
            if triangular:
                results.append(f"{num} is triangular.")
            

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


