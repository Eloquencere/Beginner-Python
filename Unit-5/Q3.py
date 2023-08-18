import tkinter as tk

count = {"A": 0, "T": 0, "C": 0, "G": 0}


def increment():
    for i in DNA.get():
        if i in "ATCG":
            count[i] += 1
    Let_Count.set(
        "A:{0}\nT:{1}\nC:{2}\nG:{3}".format(
            count["A"], count["T"], count["C"], count["G"]
        )
    )


# Creation of window
window = tk.Tk()

# Input frame
IpFrame = tk.Frame(window)
IpFrame.pack()

# Creation of a Variable string place holder
DNA = tk.StringVar()

# Creating a text box to type
entry = tk.Entry(IpFrame, textvariable=DNA)
entry.pack()
# Calculate button
button = tk.Button(IpFrame, text="Calculate", command=increment)
button.pack()

# Display Frame
DispFrame = tk.Frame(window)
DispFrame.pack()

# Initialising Display variables
Let_Count = tk.StringVar()

# Displaying Values
Disp = tk.Label(DispFrame, textvariable=Let_Count)
Disp.pack()

# Keeping the window open for inputs forever
window.mainloop()
