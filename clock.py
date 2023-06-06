#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:22:57 2023

@author: evangelosdiakatossaoulas
"""

import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x200")

is_24_hour_format = tk.BooleanVar()
is_24_hour_format.set(True)

clock_label = tk.Label(root, font=('times', 20, 'bold'), bg='white')
clock_label.pack()

def update_time():
    if is_24_hour_format.get():
        current_time = time.strftime("%H:%M:%S") # 24 hour format
    else:
        current_time = time.strftime("%I:%M:%S %p") # 12 hour format

    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

def toggle_time_format():
    is_24_hour_format.set(not is_24_hour_format.get())
    if is_24_hour_format.get():
        switch_button.config(text="24H", bg="red", fg="black")
    else:
        switch_button.config(text="12H", bg="black", fg="red")

switch_button = tk.Button(root, text="24H", bg="red", fg="black", command=toggle_time_format)
switch_button.pack()

update_time()
root.mainloop()
