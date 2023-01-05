import math
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

window = tk.Tk()
window.title("arabian number convert to roman")

def roman_num():
    # Get the base and height of the triangle from the input fields
    num = num_entry.get()

    if num.isnumeric():
        num = int(num)
        if num < 1001:
            lookup = [
                (1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I'),
            ]
            res = ''
            for (n, roman) in lookup:
                (d, num) = divmod(num, n)
                res += roman * d

            result_label.config(text=f"roman number is: \n {res} ", font=('Times', 14))
            result_label.place(x=10, y=20)
        else:
            result_label.config(text=f"enter a number\n up to 1001 ", font=('Times', 14))
            result_label.place(x=10, y=20)
    else:
        result_label.config(text=f"enter a number\n up to 1001 ", font=('Times', 14))
        result_label.place(x=10, y=20)


frame = tk.Frame(master=window, width=150, height=120)
frame.pack(fill=tk.Y, side=tk.LEFT)

frame1 = tk.Frame(master=window, width=150, height=120, bg="white")
frame1.pack(fill=tk.Y, side=tk.LEFT)




result_label = tk.Label(frame1, text="", bg = "white")
result_label.place(x=20, y=10)

instruct_label = tk.Label(text="Enter number:", font=('Times', 12))
instruct_label.place(x=45, y=5)


num_label = tk.Label(text="num:", font=('Times', 12))
num_label.place(x=5, y=35)
num_entry = tk.Entry(width=10)
num_entry.place(x=60, y=40)



calculate_button = tk.Button(text="Calculate", command=roman_num, font=('Times', 12))
calculate_button.place(x=45, y=80)





window.mainloop()