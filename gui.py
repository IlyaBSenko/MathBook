import tkinter as tk
from properties_logic import *

def button_click(event=None, result_widget=None):       
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
        factorial = is_factorial(num)
        fibonacci = is_fibonacci(num)
        sublime = is_sublime(num)
        triangular = is_triangular(num)
        palindrome = is_palindrome(num)
        armstrong = is_armstrong(num)
        perfect_square_root = is_perfect_SR(num)
        square_root = get_square_root(num)
        multiples = get_multiples(num)
        perfect_square = is_perfect_square(num)
        abundant = is_abundant(num)
        automorphic = is_automorphic(num)

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
            (perfect_square, f"{num} is a perfect square."),
            (abundant, f"{num} is abundant."),
            (automorphic, f"{num} is automorphic.")
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
    event = event or type('Event', (object,), {'widget': searchEntry})()  
    button_click_callback(event, result_text)

def create_search_window(title, button_click_callback):
    clear_window()

    title_label = tk.Label(window, text=title, font=("Arial", 14, "bold"))
    title_label.pack(pady=10)

    entry_frame = tk.Frame(window)
    entry_frame.pack(pady=5)

    searchEntry = tk.Entry(entry_frame)
    searchEntry.pack(side="left", fill="x", expand=True)

    search_button = tk.Button(entry_frame, text="Search", command=lambda: update_results(None, result_text, button_click_callback, searchEntry))
    search_button.pack(side="right", padx=5)

    result_text = tk.Text(window, height=10, width=50)
    result_text.pack(pady=10)

    searchEntry.bind("<Return>", lambda event: update_results(event, result_text, button_click_callback, searchEntry))

    back_button = tk.Button(window, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(pady=10)

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def show_main_menu():
    clear_window()

    label1 = tk.Label(window, text="Hello! Welcome to MathBook!")
    label1.pack()

    label2 = tk.Label(window, text="Click what you would like to learn!")
    label2.pack()

    button1 = tk.Button(window, text="Properties", command=show_search_entry_prop)
    button2 = tk.Button(window, text="Trivia", command=show_search_entry_trivia)
    button3 = tk.Button(window, text="Lore", command=show_search_entry_lore)
    button4 = tk.Button(window, text="Definitions", command=show_search_entry_definitions)
    button5 = tk.Button(window, text="Real World Applications", command=show_search_entry_RW)
    button1.pack(pady=5)
    button2.pack(pady=5)
    button3.pack(pady=5)
    button4.pack(pady=5)
    button5.pack(pady=5)

def show_search_entry_prop():
    create_search_window("Properties", button_click)

def show_search_entry_trivia():
    create_search_window("Trivia", button_click)

def show_search_entry_lore():
    create_search_window("Lore", button_click)

def show_search_entry_definitions():
    create_search_window("Definitions", button_click)

def show_search_entry_RW():
    create_search_window("Real World Applications", button_click)

window = tk.Tk()
window.title("MathBook")

show_main_menu()

