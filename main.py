from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import requests


def rates():
    # Get selected currencies
    from_currency = box1.get().split()[0]
    to_currency = box2.get().split()[0]

    # Fetch exchange rates
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{from_currency.lower()}.json"
    response = requests.get(url)
    rates = response.json()

    # Calculate the conversion result
    if from_currency == to_currency:
        result = float(user_input.get())
    else:
        result = float(user_input.get()) * rates[from_currency.lower()][to_currency.lower()]

    # Display the result
    if hasattr(root, 'exchange'):
        root.exchange.config(text=f"{float(user_input.get()):.2f} {from_currency} is {result:.2f} {to_currency}.")
    else:
        root.exchange = tk.Label(result_frame, font=("Sans Serif", 24), bg="#114149",
                                 text=f"{float(user_input.get()):.2f} {from_currency} is {result:.2f} {to_currency}.",
                                 fg="white")
        root.exchange.pack(side="top", pady=10)


def reset():
    # Reset input fields and dropdowns to defaults
    user_input.delete(0, tk.END)
    box1.current(92)
    box2.current(248)

    # Clear displayed exchange result
    if hasattr(root, "exchange"):
        root.exchange.destroy()
        del root.exchange


root = tk.Tk()
root.title("Currency Converting App")
root.configure(bg="#114149")

# Set application icon
icon = ImageTk.PhotoImage(Image.open("money.jpeg"))
root.iconphoto(False, icon)

# Set window size and placement
WIDTH = 800
HEIGHT = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_offset = (screen_width // 2) - (WIDTH // 2)
y_offset = (screen_height // 2) - (HEIGHT // 2)
root.geometry(f"{WIDTH}x{HEIGHT}+{x_offset}+{y_offset}")

# Frame for the title
frame1 = tk.Frame(root, bg="#114149")
frame1.pack(side="top", fill=tk.X)
title = tk.Label(frame1, text="Currency Converter 3000", bg="#114149", fg="red", font=("Helvetica", 24))
title.pack(side="top", padx=10, pady=10)

# Frame for dropdown and input fields
dropdown_frame = tk.Frame(root, bg="#114149")
dropdown_frame.pack(side="top", fill=tk.X)
enter = tk.Label(dropdown_frame, font=("Helvetica", 14), text="Enter the amount: ", bg="#114149", fg="white")
enter.grid(column=0, row=0, pady=10, padx=2)

# Fetch list of currencies
url = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json"
response = requests.get(url)
currencies = response.json()
options = [f"{key.upper()} - {value}" for key, value in currencies.items() if len(key) == 3]

# Input amount and dropdown menus
clicked = tk.StringVar()
clicked.set(options[0])
clicked2 = tk.StringVar()
clicked2.set(options[0])

user_input = tk.Entry(dropdown_frame, width=10)
user_input.grid(column=1, row=0, padx=6, pady=10)

box1 = ttk.Combobox(dropdown_frame, values=options)
box1.current(92)  # Set initial currency for the first dropdown
box1.grid(column=2, row=0, padx=10, pady=10)

label2 = tk.Label(dropdown_frame, bg="#114149", text="To", font=("Default", 24), fg="white")
label2.grid(column=3, row=0, pady=10)

box2 = ttk.Combobox(dropdown_frame, values=options)
box2.current(248)  # Set initial currency for the second dropdown
box2.grid(column=4, row=0, padx=20, pady=10)

# Convert button
convert = tk.Button(dropdown_frame, text="Convert", font=("Helvetica", 24), command=rates)
convert.grid(column=5, row=0, padx=10, pady=10)

# Frame to display the conversion result
result_frame = tk.Frame(root, bg="#114149")
result_frame.pack(side="top", fill=tk.X)

# Bottom frame with reset button
bottom_frame = tk.Frame(root, bg="#114149")
bottom_frame.pack(side="bottom", fill=tk.X)
reset_button = tk.Button(bottom_frame, font=("Sans Serif", 24), text="Reset", command=reset)
reset_button.pack(pady=20)

root.mainloop()
