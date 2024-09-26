import customtkinter as ctk
from tkinter import *

def set_window_properties(self, window_size, window_title, window_width, window_height, icon_path):
    self.geometry(window_size)
    self.title('Schmidt System - ' + window_title)
    self.resizable(window_width, window_height)
    self.iconbitmap(icon_path)

# sticky options = w, n, e, s

import customtkinter as ctk

def create_label(self=None, title=None, font=None, font_size=None, width=None, height=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None):
    self.label = ctk.CTkLabel(self, text=title, font=(font, font_size), width=width, height=height)
    self.label.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return self.label

def create_option_menu(self=None, options=None, function=None, width=None, height=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None):
    self.option_menu = ctk.CTkOptionMenu(self, values=options, command=function, width=width, height=height)
    self.option_menu.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return self.option_menu

def create_button(self=None, text=None, function=None, width=None, height=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None):
    self.button = ctk.CTkButton(self, text=text, command=function, width=width, height=height)
    self.button.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return self.button

def create_slider(master=None, minimum=None, maximum=None, function=None, width=None, height=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None):
    if width is None:
        width = 200
    if height is None:
        height = 10

    slider = ctk.CTkSlider(master, from_=minimum, to=maximum, command=function, width=width, height=height)
    slider.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)

    return slider

def create_entry(self=None, text=None, width=None, height=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None):
    self.entry = ctk.CTkEntry(self, placeholder_text=text, width=width, height=height)
    self.entry.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return self.entry

def create_progress_bar(self=None, width=None, height=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None, initial=None):
    self.progress_bar = ctk.CTkProgressBar(self, width=width, height=height)
    self.progress_bar.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    self.progress_bar.set(initial)
    return self.progress_bar

def create_switch(self=None, text=None, function=None, width=None, height=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None):
    self.switch = ctk.CTkSwitch(self, text=text, command=function, width=width, height=height)
    self.switch.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return self.switch

def create_text(self=None, width=None, height=None, bg=None, row=None, column=None, padx=None, pady=None, columnspan=None, sticky=None):
    self.text = Text(self, width=width, height=height, bg=bg)
    self.text.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)
    return self.text

def center_window(self, WINDOW_WIDTH, WINDOW_HEIGHT):
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    position_right = int(screen_width / 2 - WINDOW_WIDTH / 2)
    position_top = int(screen_height / 2 - WINDOW_HEIGHT / 2)
    self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{position_right}+{position_top}")

'''
RADIO BUTTON:
self.string_var = ctk.StringVar(value="Option 1")
self.radio_button = ctk.CTkRadioButton(self, text="Option 1", variable=self.string_var, value="Option 1",
                                       command=self.on_radio_select)
self.radio_button.grid(row=7, column=0, padx=10, pady=5, columnspan=1, sticky="w")
self.radio_button = ctk.CTkRadioButton(self, text="Option 2", variable=self.string_var, value="Option 2",
                                       command=self.on_radio_select)
self.radio_button.grid(row=8, column=0, padx=10, pady=5, columnspan=1, sticky="w")

CHECKBOX:
self.boolean_var = ctk.BooleanVar()
self.checkbox = ctk.CTkCheckBox(self, text="Check me", variable=self.boolean_var,
                                command=self.on_checkbox_toggle)
self.checkbox.grid(row=9, column=0, padx=10, pady=5, columnspan=1, sticky="w")
'''