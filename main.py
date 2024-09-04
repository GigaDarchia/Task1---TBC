from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


def rates():

    currencies = {"GEL": {"USD": 0.37, "EUR": 0.34},
                  "USD": {"GEL": 2.69, "EUR": 0.9},
                  "EUR": {"GEL": 2.97, "USD": 1.11}}

    from_currency = box1.get().split()[0]
    to_currency = box2.get().split()[0]

    if from_currency == to_currency:
        result = user_input.get()
    else:
        result = float(user_input.get()) * currencies[from_currency][to_currency]

    if hasattr(root, 'exchange'):
        root.exchange.config(text=f"{user_input.get()} {from_currency} is {result} {to_currency}.")
    else:
        root.exchange = tk.Label(result_frame, font=("Sans Serif", 24), bg="#114149",
                                 text=f"{user_input.get()} {from_currency} is {result} {to_currency}.", fg="white")
        root.exchange.pack(side="top", pady=10)


def reset():
    user_input.delete(0, tk.END)
    box1.current(0)
    box2.current(1)

    if hasattr(root, "exchange"):
        root.exchange.destroy()
        del root.exchange


root = tk.Tk()

root.title("Currency Exchange App")

root.configure(bg="#114149")

icon = ImageTk.PhotoImage(Image.open("money.jpeg"))

root.iconphoto(False, icon)

WIDTH = 800
HEIGHT = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_offset = (screen_width // 2) - (WIDTH // 2)
y_offset = (screen_height // 2) - (HEIGHT // 2)

root.geometry(f"{WIDTH}x{HEIGHT}+{x_offset}+{y_offset}")

frame1 = tk.Frame(root, bg="#114149")
frame1.pack(side="top", fill=tk.X)

title = tk.Label(frame1, text="Currency Exchanger 3000", bg="#114149", fg="red", font=("Helvetica", 24))
title.pack(side="top", padx=10, pady=10)

dropdown_frame = tk.Frame(root, bg="#114149")
dropdown_frame.pack(side="top", fill=tk.X)

enter = tk.Label(dropdown_frame, font=("Helvetica", 14), text="Enter the amount: ", bg="#114149", fg="white")
enter.grid(column=0, row=0, pady=10, padx=2)


options = ["GEL - Georgian Lari",
           "USD - US Dollar",
           "EUR - Euro"]

clicked = tk.StringVar()
clicked.set(options[0])

clicked2 = tk.StringVar()
clicked2.set(options[1])

user_input = tk.Entry(dropdown_frame, width=10)
user_input.grid(column=1, row=0, padx=6, pady=10)

box1 = ttk.Combobox(dropdown_frame, values=options)
box1.current(0)
box1.grid(column=2, row=0, padx=10, pady=10)

label2 = tk.Label(dropdown_frame, bg="#114149", text="To", font=("Default", 24), fg="white")
label2.grid(column=3, row=0, pady=10)

box2 = ttk.Combobox(dropdown_frame, values=options)
box2.current(1)
box2.grid(column=4, row=0, padx=20, pady=10)

convert = tk.Button(dropdown_frame, text="Convert", font=("Helvetica", 24), command=rates)
convert.grid(column=5, row=0, padx=10, pady=10)

result_frame = tk.Frame(root, bg="#114149")
result_frame.pack(side="top", fill=tk.X)


bottom_frame = tk.Frame(root, bg="#114149")
bottom_frame.pack(side="bottom", fill=tk.X)

reset_button = tk.Button(bottom_frame, font=("Sans Serif", 24), text="Reset", command=reset)
reset_button.pack(pady=20)

root.mainloop()
