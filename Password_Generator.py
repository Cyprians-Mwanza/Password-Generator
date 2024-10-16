import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog

import strength_checker  # Importing the custom password strength checker module


def center_window(root, width=400, height=300):
    # Get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    # Set the geometry of the window
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')


def get_user_preferences():
    # Retrieve user preferences for password generation from the UI
    length = int(length_var.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    return length, include_uppercase, include_lowercase, include_digits, include_special


def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    # Build the character set based on user preferences
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Raise an error if no character types are selected
    if not characters:
        raise ValueError("No character types selected! At least one type must be included.")

    # Generate the password by randomly selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def generate_and_display_password():
    try:
        # Get user preferences and generate a password
        length, include_uppercase, include_lowercase, include_digits, include_special = get_user_preferences()
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        # Check the strength of the generated password
        strength = strength_checker.check_password_strength(password)
        # Display the generated password and its strength
        result_var.set(f"Generated Password: {password}\nPassword Strength: {strength}")
    except ValueError as e:
        # Show an error message if something goes wrong
        messagebox.showerror("Error", str(e))


def save_password():
    # Extract the password from the result label
    password = result_var.get().split('\n')[0].split(': ')[1]
    # Prompt the user to select a file path to save the password
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        # Write the password to the selected file
        with open(file_path, 'w') as file:
            file.write(password)
        # Show a confirmation message after saving the password
        messagebox.showinfo("Save Password", f"Password saved successfully at {file_path}!")


# Tkinter UI setup
root = tk.Tk()
root.title("Password Generator")

# Center the window
center_window(root, 400, 300)

# Using grid layout for better alignment
main_frame = tk.Frame(root)
main_frame.pack(pady=20)

# Label and entry for password length
length_label = tk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky='e')
length_var = tk.IntVar()
length_entry = tk.Entry(main_frame, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Checkbuttons for including character types
uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(main_frame, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')

lowercase_var = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(main_frame, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

digits_var = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(main_frame, text="Include Digits", variable=digits_var)
digits_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='w')

special_var = tk.BooleanVar(value=True)
special_check = tk.Checkbutton(main_frame, text="Include Special Characters", variable=special_var)
special_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='w')

# Button to generate password
generate_button = tk.Button(main_frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=5, column=0, columnspan=2, pady=10)

# Label to display the result
result_var = tk.StringVar()
result_label = tk.Label(main_frame, textvariable=result_var, wraplength=300)
result_label.grid(row=6, column=0, columnspan=2, pady=5)

# Button to save the password
save_button = tk.Button(main_frame, text="Save Password", command=save_password)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
