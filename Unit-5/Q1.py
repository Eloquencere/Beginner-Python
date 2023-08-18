import tkinter as tk

# Window Creation
window = tk.Tk()

# Button Creation and packing
button = tk.Button(window, text="Goodbye", command=lambda: window.destroy())
button.pack()

# Keeping the window open for inputs forever
window.mainloop()
