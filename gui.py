"""
gui.py
-------
This module provides the graphical user interface (GUI) for the MathBook application.
It uses tkinter to create windows, buttons, text entry widgets, and other components that allow
the user to interact with various mathematical topics such as Properties, Trivia, Lore,
Definitions, and Real World Applications.
"""

import tkinter as tk  

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
        user_inp = event.widget.get().strip()
        num = int(user_inp)

        prime = is_prime(num)                   
        parity = parity_checker(num)            
        perfect = is_perfect(num)               
        composite = is_composite(num)           
        square = square_checker(num)            
        cube = cube_checker(num)                
        divisors = get_divisors(num)            
        factorial = compute_factorial(num)      
        fibonacci = is_fibonacci(num)           
        sublime = is_sublime(num)               
        triangular = is_triangular(num)         
        palindrome = is_palindrome(num)         
        armstrong = is_armstrong(num)           
        perfect_square_root = get_perfect_square_root(num)  
        square_root = get_square_root(num)      
        multiples = get_multiples(num)          
        perfect_square = is_perfect_square(num) 
        abundant = is_abundant(num)             
        deficient = is_deficient(num)           
        automorphic = is_automorphic(num)
        alphabetical = is_alphabetical(num)

        results = []  

        results.append(f"{num} is {parity}.")

        if num < 0:
            results.append(f"{num} is negative and does not have properties like prime, composite, or multiples")
        
        if num == 0:
            results.append(f"{num} is a multiple of every number.")  
            results.append(f"Every non-zero number is considered a divisor of {num}")
        else:
            results.append(f"The first 5 multiples of {num} are {multiples}")
            results.append(f"Divisors: {divisors}")

        if not perfect_square_root:
            results.append(f"The square root of {num} is {square_root}")

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
            (deficient, f"{num} is deficient"),
            (alphabetical, f"{num} is alphabetical")
        ]
        for condition, message in property_checks:
            if condition:
                results.append(message)

        if perfect_square_root:
            results.append(f"The square root of {num} is {perfect_square_root}")

        if factorial is None:
            results.append("Number too big to check for factorial!")
        else:
            results.append(f"The factorial of {num} is ({factorial}!)")
    
        if isinstance(result_widget, tk.Text):
            result_widget.delete(1.0, tk.END)  
            result_widget.insert(tk.END, "\n".join(results)) 
        else:
            result_widget.config(text="\n".join(results))  
    
    except ValueError:
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
    event = event or type('Event', (object,), {'widget': searchEntry})()
    button_click_callback(event, result_text)

def create_search_window(title, button_click_callback):
    """
    Creates a generic search window with a title, an input field, a search button, and a result display.
    
    This is used for topics that use a search-based interface.
    
    :param title: The title to display at the top of the window.
    :param button_click_callback: The callback function to process the search input.
    """
    clear_window()  
        

    title_label = tk.Label(window, text=title, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    entry_frame = tk.Frame(window)
    entry_frame.pack(pady=5)

    searchEntry = tk.Entry(entry_frame)
    searchEntry.pack(side="left", fill="x", expand=True)

    search_button = tk.Button(entry_frame, text="Search",
                              command=lambda: update_results(None, result_text, button_click_callback, searchEntry))
    search_button.pack(side="right", padx=5)

    result_text = tk.Text(window, height=10, width=50)
    result_text.pack(pady=10)

    searchEntry.bind("<Return>", lambda event: update_results(event, result_text, button_click_callback, searchEntry))

    back_button = tk.Button(window, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=10)

def clear_window():
    """
    Clears the current window by destroying all its child widgets.
    """
    for widget in window.winfo_children():
        widget.destroy()

def show_main_menu():
    """
    Displays the main menu of the MathBook application.
    
    The main menu offers buttons for Properties, Trivia, Lore, Definitions, and Real World Applications.
    """
    clear_window()  

    label1 = tk.Label(window, text="Hello! Welcome to MathBook!")
    label1.pack()
    label2 = tk.Label(window, text="Click what you would like to learn!")
    label2.pack()

    button1 = tk.Button(window, text="Properties", command=show_search_entry_prop)
    button2 = tk.Button(window, text="Trivia", command=show_search_entry_trivia)
    button3 = tk.Button(window, text="Lore", command=show_search_entry_lore)
    button4 = tk.Button(window, text="Definitions", command=show_definitions_menu)  
    button5 = tk.Button(window, text="Real World Applications", command=show_search_entry_RW)

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
    clear_window()  

    title_label = tk.Label(window, text="Definitions", font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    for property_name in get_property_names():
        property_button = tk.Button(window, text=property_name,
                                    command=lambda p=property_name: show_definition(p))
        property_button.pack(pady=5, fill="x")

    back_button = tk.Button(window, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=10)


# FIXME: button layout for definitions
def show_definition(property_name):
    """
    Displays the definition of a selected property.
    
    :param property_name: The name of the property to display.
    """
    clear_window()  

    title_label = tk.Label(window, text=property_name, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    definition = get_property_definition(property_name)
    definition_label = tk.Label(window, text=definition, wraplength=500, justify="left")
    definition_label.pack(pady=10)

    back_button = tk.Button(window, text="Back to Definitions Menu", command=show_definitions_menu)
    back_button.pack(pady=10)

# FIXME: finish searchentry real world
def show_search_entry_RW():
    """
    Opens the search window for the Real World Applications topic.
    """
    clear_window() 
    
    title_label = tk.Label(window, text=property_name, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)
    
    definition = get_property_definition(property_name)
    create_search_window("Real World Applications", button_click)

window = tk.Tk()           
window.title("MathBook")  

show_main_menu()  
