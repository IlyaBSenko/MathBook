import tkinter as tk
from logic import *

# Function to handle a button click
def button_click(event=None):  # Accept the event parameter for key bindings
    try:
        user_inp = searchEntry.get().strip()
        num = int(user_inp)

        # Call logic functions and get results
        prime = prime_checker(num)
        parity = parity_checker(num)
        perfect = perfect_number_checker(num)
        composite = composite_checker(num)

        # Format results
        results = []
        results.append(f"{num} is {parity}.")

        if num <= 0:
            results.append(f"{num} is neither prime nor composite.")
        else:
            if prime:
                results.append(f"{num} is prime.")
            if composite:
                results.append(f"{num} is composite.")
            if perfect:
                results.append(f"{num} is perfect.")

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


