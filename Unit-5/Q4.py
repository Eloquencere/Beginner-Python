import tkinter as tk

# Calculating Celcuis equivalent
def calc():
    Celci.set((faren.get() - 32) * (5 / 9))


# Creation of window
window = tk.Tk()

# Label1
Label1 = tk.Label(window, text="Enter Temperature in Farenheit")
Label1.pack()

# Creation of TextBox
faren = tk.IntVar()
box = tk.Entry(window, textvariable=faren)
box.pack()

# Calculate Button
button1 = tk.Button(window, text="Calculate", command=calc)
button1.pack()
button2 = tk.Button(window, text="Quit", command=lambda: window.destroy())
button2.pack()

# Display Value
Celci = tk.IntVar()
Label2 = tk.Label(window, textvariable=Celci)
Label2.pack()

# Keeping the window open for inputs forever
window.mainloop()
