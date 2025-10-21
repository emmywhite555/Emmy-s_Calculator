import tkinter as tk

# Function to update the expression
def press(num):
    entry_field.insert(tk.END, num)

# Function to clear the entry field
def clear():
    entry_field.delete(0, tk.END)

# Function to evaluate the expression
def equal():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Entry field
entry_field = tk.Entry(window, font=("Arial", 18), borderwidth=4, relief="ridge", justify="right")
entry_field.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, padx=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == 'C':
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=clear)
    elif text == '=':
        btn = tk.Button(window, text=text, width=24, height=2, font=("Arial", 14), command=equal)
        btn.grid(row=row, column=col, columnspan=4, pady=10, padx=10)
        continue
    else:
        btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, pady=5, padx=5)

# Run the main loop
window.mainloop()
