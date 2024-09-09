import tkinter as tk
from tkinter import messagebox

# Define the graphical password as a sequence of button clicks
password_sequence = ['btn1', 'btn2', 'btn3', 'btn4']
input_sequence = []

def button_click(button_id):
    # Add the clicked button to the input sequence
    input_sequence.append(button_id)
    
    # Check if input sequence matches the password
    if len(input_sequence) == len(password_sequence):
        if input_sequence == password_sequence:
            messagebox.showinfo("Success", "Password Correct! Access Granted.")
        else:
            messagebox.showerror("Error", "Password Incorrect! Try Again.")
        # Reset the input sequence after checking
        input_sequence.clear()

# Set up the tkinter GUI
root = tk.Tk()
root.title("Graphical Password Authentication")

# Create buttons for graphical password input
btn1 = tk.Button(root, text="Button 1", width=10, height=5, command=lambda: button_click('btn1'))
btn2 = tk.Button(root, text="Button 2", width=10, height=5, command=lambda: button_click('btn2'))
btn3 = tk.Button(root, text="Button 3", width=10, height=5, command=lambda: button_click('btn3'))
btn4 = tk.Button(root, text="Button 4", width=10, height=5, command=lambda: button_click('btn4'))

# Position buttons in the GUI
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)

# Start the main GUI loop
root.mainloop()
