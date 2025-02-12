"""
gui.py
-------
This module provides the graphical user interface (GUI) for the MathBook application.
It uses tkinter to create windows, buttons, text entry widgets, and other components that allow
the user to interact with various mathematical topics such as Properties, Trivia, Lore,
Definitions, and Real World Applications.
"""

import tkinter as tk  # Import tkinter for creating the GUI

# Import all functions from properties_logic and definitions modules for use in the GUI.
from properties_logic import *
from definitions import *

def button_click(event=None, result_widget=None):
    """
    Handles the event triggered by clicking the search button or pressing the Return key.
    
    This function reads the user's input from the widget (provided by the event), converts it to
    an integer, and then computes various mathematical properties using helper functions.
    The results are then displayed in the specified result_widget (which can be a Text or Label widget).

    :param event: The event that triggered the function (default is None).
    :param result_widget: The widget (Text or Label) where the results will be displayed.
    """
    try:
        # Retrieve the text from the widget that triggered the event and remove extra whitespace
        user_inp = event.widget.get().strip()
        # Convert the user input into an integer value
        num = int(user_inp)

        # Calculate various mathematical properties using helper functions from properties_logic
        prime = is_prime(num)                 # True if num is prime, else False
        parity = parity_checker(num)          # Returns "even" or "odd" based on num's parity
        perfect = is_perfect(num)             # True if num is a perfect number, else False
        composite = is_composite(num)         # True if num is composite, else False
        square = square_checker(num)          # True if num is a perfect square, else False
        cube = cube_checker(num)              # True if num is a perfect cube, else False
        divisors = get_divisors(num)          # List of all divisors of num
        factorial = is_factorial(num)         # Factorial of num if num is small enough; else None
        fibonacci = is_fibonacci(num)         # True if num is in the Fibonacci sequence, else False
        sublime = is_sublime(num)             # True if num is a sublime number, else False
        triangular = is_triangular(num)       # True if num is a triangular number, else False
        palindrome = is_palindrome(num)       # True if num is a palindrome, else False
        armstrong = is_armstrong(num)         # True if num is an Armstrong number, else False
        perfect_square_root = is_perfect_SR(num)  # Returns the integer square root if perfect, else False or 0
        square_root = get_square_root(num)    # The square root of num formatted to 3 decimal places (if applicable)
        multiples = get_multiples(num)        # First five multiples of num
        perfect_square = is_perfect_square(num)  # True if num is a perfect square, else False
        abundant = is_abundant(num)           # True if num is abundant, else False
        deficient = is_deficient(num)         # True if num is deficient, else False
        automorphic = is_automorphic(num)     # True if num is automorphic, else False

        results = []  # Create an empty list to collect all result messages
        results.append(f"{num} is {parity}.")  # Add a message about num's parity (even or odd)

        # Special handling for negative numbers
        if num < 0:
            results.append(f"{num} is negative and does not have properties like prime, composite, or multiples")
            
        # Special handling for the number zero
        if num == 0:
            results.append(f"{num} is a multiple of every number.")  # 0 is a multiple of every number
            results.append(f"Every non-zero number is considered a divisor of {num}")  # Special divisor case for 0
        else:
            results.append(f"The first 5 multiples of {num} are {multiples}")  # Display the first five multiples
            results.append(f"Divisors: {divisors}")  # Display the divisors of num
            
        # If num is not a perfect square (as determined by is_perfect_SR), then show the calculated square root
        if not perfect_square_root:
            results.append(f"The square root of {num} is {square_root}")
            
        # Prepare a list of tuples where each tuple holds a condition and its corresponding message
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
            (armstrong, f"{num} is an armstrong number"),
            (perfect_square, f"{num} is a perfect square"),
            (abundant, f"{num} is abundant"),
            (automorphic, f"{num} is automorphic"),
            (deficient, f"{num} is deficient")
        ]

        # Iterate through each property check and add the message if the condition is True
        for condition, message in property_checks:
            if condition:
                results.append(message)
        
        # If a perfect square root exists, add it to the results
        if perfect_square_root:
            results.append(f"The square root of {num} is {perfect_square_root}")
        
        # Handle the factorial result (None indicates the number is too big to compute a factorial)
        if factorial == None:
            results.append(f"Number too big to check for factorial!")
        else:
            results.append(f"The factorial of {num} is ({factorial}!)")
    
        # Display the results in the result_widget. The widget could be a Text or Label widget.
        if isinstance(result_widget, tk.Text):
            result_widget.delete(1.0, tk.END)  # Clear any previous content
            result_widget.insert(tk.END, "\n".join(results))  # Insert the new results
        else:
            result_widget.config(text="\n".join(results))  # Set the text for a Label widget

    except ValueError:
        # If converting the input to an integer fails, display an error message.
        if isinstance(result_widget, tk.Text):
            result_widget.delete(1.0, tk.END)
            result_widget.insert(tk.END, "Please enter a valid number.")
        elif isinstance(result_widget, tk.Label):
            result_widget.config(text="Please enter a valid number.")

def update_results(event, result_text, button_click_callback, searchEntry):
    """
    Triggers the button click callback to update the results.

    If no event is provided, it creates a dummy event using the searchEntry widget.
    
    :param event: The event object from the widget (or None).
    :param result_text: The widget where the result text is displayed.
    :param button_click_callback: The callback function to process the search input.
    :param searchEntry: The Entry widget where the user types the input.
    """
    # If event is None, create a dummy event with the searchEntry widget attached.
    event = event or type('Event', (object,), {'widget': searchEntry})()
    # Call the provided callback function to process the input and update the result_text widget.
    button_click_callback(event, result_text)

def create_search_window(title, button_click_callback):
    """
    Creates a search window with a title, input field, search button, and result display area.

    This function clears the current window, displays the given title, and creates an Entry widget
    for user input. It also adds a Search button and binds the Return key to perform the search.

    :param title: The title to display at the top of the window.
    :param button_click_callback: The callback function to process the search input.
    """
    clear_window()  # Remove all widgets from the current window

    # Create a label with the title and add it to the window
    title_label = tk.Label(window, text=title, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Create a frame to hold the search entry and search button
    entry_frame = tk.Frame(window)
    entry_frame.pack(pady=5)

    # Create the Entry widget where the user can type their search term
    searchEntry = tk.Entry(entry_frame)
    searchEntry.pack(side="left", fill="x", expand=True)

    # Create the Search button and set its command to update the results when clicked
    search_button = tk.Button(entry_frame, text="Search", command=lambda: update_results(None, result_text, button_click_callback, searchEntry))
    search_button.pack(side="right", padx=5)

    # Create a Text widget to display the search results
    result_text = tk.Text(window, height=10, width=50)
    result_text.pack(pady=10)

    # Bind the Return key to trigger the search
    searchEntry.bind("<Return>", lambda event: update_results(event, result_text, button_click_callback, searchEntry))

    # Create a Back button to return to the main menu
    back_button = tk.Button(window, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=10)

def clear_window():
    """
    Clears the current window by destroying all of its child widgets.
    """
    # Loop through every widget in the window and destroy it
    for widget in window.winfo_children():
        widget.destroy()

def show_main_menu():
    """
    Displays the main menu of the MathBook application.

    The main menu provides buttons for various topics: Properties, Trivia, Lore, Definitions, and
    Real World Applications.
    """
    clear_window()  # Remove existing widgets from the window

    # Create and display a welcome message
    label1 = tk.Label(window, text="Hello! Welcome to MathBook!")
    label1.pack()

    # Create and display an instruction message
    label2 = tk.Label(window, text="Click what you would like to learn!")
    label2.pack()

    # Create buttons for each topic and assign corresponding functions to be called when clicked
    button1 = tk.Button(window, text="Properties", command=show_search_entry_prop)
    button2 = tk.Button(window, text="Trivia", command=show_search_entry_trivia)
    button3 = tk.Button(window, text="Lore", command=show_search_entry_lore)
    button4 = tk.Button(window, text="Definitions", command=show_search_entry_definitions)
    button5 = tk.Button(window, text="Real World Applications", command=show_search_entry_RW)
    # Display the buttons with some vertical padding
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(pady=5)
    button4.pack(pady=5)
    button5.pack(pady=5)

def show_search_entry_prop():
    """
    Opens the search window for the Properties topic.
    
    Utilizes create_search_window with "Properties" as the title.
    """
    create_search_window("Properties", button_click)

def show_search_entry_trivia():
    """
    Opens the search window for the Trivia topic.
    
    Utilizes create_search_window with "Trivia" as the title.
    """
    create_search_window("Trivia", button_click)

def show_search_entry_lore():
    """
    Opens the search window for the Lore topic.
    
    Utilizes create_search_window with "Lore" as the title.
    """
    create_search_window("Lore", button_click)

def show_search_entry_definitions():
    """
    Displays the Definitions menu with buttons for each property definition.

    When a property button is clicked, the full definition of that property is shown.
    """
    clear_window()  # Clear any existing content in the window

    # Display a title for the Definitions menu
    title_label = tk.Label(window, text="Definitions", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Create a button for each property available in the definitions dictionary
    for property_name in get_property_names():
        property_button = tk.Button(window, text=property_name, command=lambda p=property_name: show_definition(p))
        property_button.pack(pady=5, fill="x")

    # Add a Back button to return to the main menu
    back_button = tk.Button(window, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=10)

def show_definition(property_name):
    """
    Displays the definition of a selected property.

    :param property_name: The name of the property whose definition should be shown.
    """
    clear_window()  # Clear the current window

    # Create and display a title label with the property name
    title_label = tk.Label(window, text=property_name, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    # Retrieve the definition for the property and create a label to display it
    definition = get_property_definition(property_name)
    definition_label = tk.Label(window, text=definition, wraplength=500, justify="left")
    definition_label.pack(pady=10)

    # Add a Back button to return to the Definitions menu
    back_button = tk.Button(window, text="Back to Definitions Menu", command=show_search_entry_definitions)
    back_button.pack(pady=10)

def show_search_entry_RW():
    """
    Opens the search window for the Real World Applications topic.
    
    Utilizes create_search_window with "Real World Applications" as the title.
    """
    create_search_window("Real World Applications", button_click)

# Create the main application window using tkinter
window = tk.Tk()           # Initialize the main window
window.title("MathBook")   # Set the window title

show_main_menu()  # Display the main menu when the application starts
