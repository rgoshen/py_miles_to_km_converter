from tkinter import *

FACTOR = 1.60934

def convert():
    num = float(miles_input.get())
    to_km = num * FACTOR
    print(conversion_label.config(text=f"{to_km:.1f}"))

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=10)

# Entires
miles_input = Entry(width=10)
miles_input.grid(column=2, row=1)
miles_input.insert(END, string="0")
miles_input.focus()

# Miles label
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)
miles_label.config(pady=5)

# Row 2 labels
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=1, row=2)
equal_to_label.config(pady=5)
conversion_label = Label(text="0")
conversion_label.grid(column=2, row=2)
conversion_label.config(pady=5)
km_label = Label(text="Km")
km_label.grid(column=3, row=2)
km_label.config(pady=5)

# Convert button
convert_button = Button(text="Convert", command=convert)
convert_button.grid(column=2, row=3)

window.mainloop()
