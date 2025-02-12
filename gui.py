"""
gui.py
-------
This module provides the graphical user interface (GUI) for the MathBook application.
It uses tkinter to create windows, buttons, text entry widgets, and other components that allow
the user to interact with various mathematical topics such as Properties, Trivia, Lore,
Definitions, and Real World Applications.
"""

import tkinter as tk  # Import tkinter to build the GUI

# Import the business logic and definitions; note these modules do NOT import GUI, avoiding circular dependencies.
from properties_logic import *
from definitions import *

def button_click(event=None, result_widget=None):
    """
    Handles the event when the user clicks the search button or presses Return.
    
    This function retrieves the user's input, converts it to an integer, computes various
    mathematical properties using helper functions, and then displays the results.
    
    :param event: The event that triggered this function.
    :param result_widget: The widget (Text or Label) where the results will be displayed.
    """
    try:
        # Get the user input from the widget and remove extra whitespace
        user_inp = event.widget.get().strip()
        # Convert the input string to an integer
        num = int(user_inp)

        # Compute various mathematical properties using the functions from properties_logic
        prime = is_prime(num)                   # Check if num is prime
        parity = parity_checker(num)            # Determine if num is even or odd
        perfect = is_perfect(num)               # Check if num is a perfect number
        composite = is_composite(num)           # Check if num is composite
        square = square_checker(num)            # Check if num is a perfect square
        cube = cube_checker(num)                # Check if num is a perfect cube
        divisors = get_divisors(num)            # Get all divisors of num
        factorial = compute_factorial(num)      # Compute factorial if num is small enough
        fibonacci = is_fibonacci(num)           # Check if num is in the Fibonacci sequence
        sublime = is_sublime(num)               # Check if num is sublime
        triangular = is_triangular(num)         # Check if num is triangular
        palindrome = is_palindrome(num)         # Check if num is a palindrome
        armstrong = is_armstrong(num)           # Check if num is an Armstrong number
        perfect_square_root = get_perfect_square_root(num)  # Get the integer square root if num is a perfect square
        square_root = get_square_root(num)      # Compute the square root (formatted) of num
        multiples = get_multiples(num)          # Get the first 5 multiples of num
        perfect_square = is_perfect_square(num) # Check if num is a perfect square
        abundant = is_abundant(num)             # Check if num is abundant
        deficient = is_deficient(num)           # Check if num is deficient
        automorphic = is_automorphic(num)       # Check if num is automorphic

        results = []  # Initialize an empty list to collect result messages

        # Add the parity result (even/odd) to the results
        results.append(f"{num} is {parity}.")

        # Special handling for negative numbers
        if num < 0:
            results.append(f"{num} is negative and does not have properties like prime, composite, or multiples")
        
        # Special handling for zero
        if num == 0:
            results.append(f"{num} is a multiple of every number.")  # For 0, every number is a multiple
            results.append(f"Every non-zero number is considered a divisor of {num}")
        else:
            # Add the first five multiples and the divisors to the results
            results.append(f"The first 5 multiples of {num} are {multiples}")
            results.append(f"Divisors: {divisors}")

        # If the number is not a perfect square (as determined by get_perfect_square_root), show the computed square root
        if not perfect_square_root:
            results.append(f"The square root of {num} is {square_root}")

        # Prepare a list of property checks along with corresponding messages
        property_checks = [
            (prime, f"{num} is prime"),
            (composite, f"{num} is composite"),
            (perfect, f"{num} is perfect"),
            (square, f"{num} is a square number"),
            (cube, f"{num} is a cube number"),
            (fibonacci, f"{num} is a Fibonacci number"),
            (sublime, f"{num} is sublime"),
            (triangular, f"{num} is triangular"),
            (palindrome, f"{num} is a palindrome"),
            (armstrong, f"{num} is an Armstrong number"),
            (perfect_square, f"{num} is a perfect square"),
            (abundant, f"{num} is abundant"),
            (automorphic, f"{num} is automorphic"),
            (deficient, f"{num} is deficient")
        ]
        # Add each property message if its corresponding condition is True
        for condition, message in property_checks:
            if condition:
                results.append(message)

        # If there is a perfect square root, add it to the results
        if perfect_square_root:
            results.append(f"The square root of {num} is {perfect_square_root}")

        # Handle the factorial result (None indicates the number is too big)
        if factorial is None:
            results.append("Number too big to check for factorial!")
        else:
            results.append(f"The factorial of {num} is ({factorial}!)")
    
        # Display the results in the result_widget; supports both Text and Label widgets
        if isinstance(result_widget, tk.Text):
            result_widget.delete(1.0, tk.END)  # Clear previous content
            result_widget.insert(tk.END, "\n".join(results))  # Insert new results
        else:
            result_widget.config(text="\n".join(results))  # For a Label widget, update its text
    
    except ValueError:
        # If the conversion to integer fails, display an error message
        if isinstance(result_widget, tk.Text):
            result_widget.delete(1.0, tk.END)
            result_widget.insert(tk.END, "Please enter a valid number.")
        elif isinstance(result_widget, tk.Label):
            result_widget.config(text="Please enter a valid number.")

def update_results(event, result_text, button_click_callback, searchEntry):
    """
    Triggers the button click callback to update the results.
    
    If no event is provided, creates a dummy event with the searchEntry widget.
    
    :param event: The event object (or None).
    :param result_text: The widget where the results are displayed.
    :param button_click_callback: The callback function to process the search.
    :param searchEntry: The Entry widget where the user types their input.
    """
    # Create a dummy event if necessary, setting its widget attribute to searchEntry
    event = event or type('Event', (object,), {'widget': searchEntry})()
    # Call the provided callback to process input and update results
    button_click_callback(event, result_text)

def create_search_window(title, button_click_callback):
    """
    Creates a generic search window with a title, an input field, a search button, and a result display.
    
    This is used for topics that use a search-based interface.
    
    :param title: The title to display at the top of the window.
    :param button_click_callback: The callback function to process the search input.
    """
    clear_window()  # Remove any existing widgets from the window

    # Create and pack a label for the title
    title_label = tk.Label(window, text=title, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Create a frame to hold the search entry and button
    entry_frame = tk.Frame(window)
    entry_frame.pack(pady=5)

    # Create the Entry widget for user input
    searchEntry = tk.Entry(entry_frame)
    searchEntry.pack(side="left", fill="x", expand=True)

    # Create the Search button and set its command to update the results
    search_button = tk.Button(entry_frame, text="Search",
                              command=lambda: update_results(None, result_text, button_click_callback, searchEntry))
    search_button.pack(side="right", padx=5)

    # Create a Text widget to display search results
    result_text = tk.Text(window, height=10, width=50)
    result_text.pack(pady=10)

    # Bind the Return key to trigger the search (using update_results)
    searchEntry.bind("<Return>", lambda event: update_results(event, result_text, button_click_callback, searchEntry))

    # Create a Back button to return to the main menu
    back_button = tk.Button(window, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=10)

def clear_window():
    """
    Clears the current window by destroying all its child widgets.
    """
    # Loop through all widgets in the window and destroy each one
    for widget in window.winfo_children():
        widget.destroy()

def show_main_menu():
    """
    Displays the main menu of the MathBook application.
    
    The main menu offers buttons for Properties, Trivia, Lore, Definitions, and Real World Applications.
    """
    clear_window()  # Clear the window before displaying new content

    # Create and pack a welcome label
    label1 = tk.Label(window, text="Hello! Welcome to MathBook!")
    label1.pack()
    # Create and pack an instruction label
    label2 = tk.Label(window, text="Click what you would like to learn!")
    label2.pack()

    # Create buttons for each topic and assign their corresponding callback functions
    button1 = tk.Button(window, text="Properties", command=show_search_entry_prop)
    button2 = tk.Button(window, text="Trivia", command=show_search_entry_trivia)
    button3 = tk.Button(window, text="Lore", command=show_search_entry_lore)
    button4 = tk.Button(window, text="Definitions", command=show_definitions_menu)  # Specialized definitions menu
    button5 = tk.Button(window, text="Real World Applications", command=show_search_entry_RW)

    # Pack each button with some vertical padding
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(pady=5)
    button4.pack(pady=5)
    button5.pack(pady=5)

def show_search_entry_prop():
    """
    Opens the search window for the Properties topic.
    """
    create_search_window("Properties", button_click)

def show_search_entry_trivia():
    """
    Opens the search window for the Trivia topic.
    """
    create_search_window("Trivia", button_click)

def show_search_entry_lore():
    """
    Opens the search window for the Lore topic.
    """
    create_search_window("Lore", button_click)

def show_definitions_menu():
    """
    Displays a specialized Definitions menu with buttons for each property definition.
    
    Clicking a property button shows its full definition.
    """
    clear_window()  # Clear any existing widgets

    # Create and pack a title label for the Definitions menu
    title_label = tk.Label(window, text="Definitions", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Loop through all property names from the definitions module
    for property_name in get_property_names():
        # Create a button for each property that will show its definition when clicked
        property_button = tk.Button(window, text=property_name,
                                    command=lambda p=property_name: show_definition(p))
        property_button.pack(pady=5, fill="x")

    # Create a Back button to return to the main menu
    back_button = tk.Button(window, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=10)

def show_definition(property_name):
    """
    Displays the definition of a selected property.
    
    :param property_name: The name of the property to display.
    """
    clear_window()  # Clear the window for the definition display

    # Create and pack a title label with the property name
    title_label = tk.Label(window, text=property_name, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Get the definition from the definitions module and create a label for it
    definition = get_property_definition(property_name)
    definition_label = tk.Label(window, text=definition, wraplength=500, justify="left")
    definition_label.pack(pady=10)

    # Create a Back button to return to the Definitions menu
    back_button = tk.Button(window, text="Back to Definitions Menu", command=show_definitions_menu)
    back_button.pack(pady=10)

def show_search_entry_RW():
    """
    Opens the search window for the Real World Applications topic.
    """
    create_search_window("Real World Applications", button_click)

# Initialize the main application window using tkinter
window = tk.Tk()           # Create the main window
window.title("MathBook")   # Set the title of the window

show_main_menu()  # Display the main menu when the application starts
