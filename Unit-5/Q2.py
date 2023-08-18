import tkinter as tk


def increment():
    count.set(count.get() + 1)


# Creation of window
window = tk.Tk()

# Initialising counter
count = tk.IntVar()
count.set(0)

# Creation of button
button = tk.Button(
    window, textvariable=count, command=increment, font=("Comic Sans MS", 50)
)
button.pack()

# Keeping the window open for inputs forever
window.mainloop()
