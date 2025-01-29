import tkinter as tk

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
button1 = tk.Button(window, text="Enter")
button1.pack() # places button on window

window.mainloop() # starts the event loop, which waits for user interaction and updates GUI
