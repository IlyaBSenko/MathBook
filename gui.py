import tkinter as tk

from logic import *

# function to handle a button click
def button_click():
    try:
        user_inp = searchEntry.get().strip()

        # convert input to an integer
        num = int(user_inp)

        # call logic functions and get results
        prime = prime_checker(num)
        parity = parity_checker(num)
        perfect = perfect_number_checker(num)
        composite = composite_checker(num)

        # format results
        results = []
        results.append(f"{num} is {parity}.")

        if prime:
            results.append(f"{num} is prime.")
        
        if composite:
            results.append(f"{num} is composite.")
        
        if perfect:
            results.append(f"{num} is perfect.")

        result_label.config(text="\n".join(results))


        #update the result label
        result_label.config(text="\n".join(results))

# main window
window = tk.Tk()
window.title("Main Window")

# label widget
label1 = tk.Label(window, text="Hello! Welcome to MathBook!")
labelBLANK = tk.Label(window, text="")
labelBLANK2 = tk.Label(window, text="")
label2 = tk.Label(window, text="Search a number!")
label1.pack() # places label on window using pack layout manager
label2.pack()
labelBLANK.pack()

# entry widget
searchEntry = tk.Entry(window, text="Search")
searchEntry.pack()
labelBLANK2.pack()
    
# button widget
button1 = tk.Button(window, text="Enter", command=button_click)
button1.pack() # places button on window

# Label to display results
result_label = tk.Label(window, text="", bg="lightgray", width=50, height=10, anchor="nw")
result_label.pack(pady=10)

window.mainloop() # starts the event loop, which waits for user interaction and updates GUI
