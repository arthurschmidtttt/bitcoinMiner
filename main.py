import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import style

ctk.set_appearance_mode('System') # (Light/Dark/System)
ctk.set_default_color_theme('green') # (green/blue/dark-blue)

WINDOW_TITLE = 'CustomTkinter - Schmidt Guide'
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 600
WINDOW_SIZE = str(WINDOW_WIDTH)+'x'+str(WINDOW_HEIGHT)
ICON_PATH = 'C:\\Users\\arthu\\PycharmProjects\\customTkinterGuide\\images\\icon.ico'

class CustomTkinterGuide(ctk.CTk):
    def __init__(self):
        super().__init__()

        style.set_window_properties(self, WINDOW_SIZE, WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, ICON_PATH)

        style.center_window(self, WINDOW_WIDTH, WINDOW_HEIGHT)

        style.create_label(self, WINDOW_TITLE, 'Arial', 24, WINDOW_WIDTH, 25,
                           row=0, column=0, pady=0, padx=0, columnspan=2, sticky='w',)

        style.create_option_menu(self, ['System', 'Light', 'Dark'], self.change_appearance_mode, 100, 25,
                                 1, 0, 10, 10, 1, 'w')

        style.create_button(self, 'Click Me', self.on_button_click, 100, 25,
                            1, 0, 10, 10, 1, 'e')

        style.create_slider(self, 0, 100, self.on_slider_change, WINDOW_WIDTH - 20, 25,
                            2, 0, 10, 10, 1, 'w')

        style.create_entry(self, 'Enter text here', 225, 30,
                           3, 0, 10, 10, 1, 'w')

        style.create_progress_bar(self, WINDOW_WIDTH - 20, 10,
                                  4, 0, 10, 10, 2, 'w',
                                  initial=0)

        style.create_button(self, 'Start Progress', self.start_progress, 100, 25,
                            5, 0, 5, 10, 1, 'w')

        style.create_button(self, 'Stop Progress', self.stop_progress, 100, 25,
                            5, 0, 5, 10, 1, 'e')

        style.create_switch(self, 'Toggle me', self.on_switch_toggle, 100, 25,
                            6, 0, 10, 10, 1, 'w')

        self.string_var = ctk.StringVar(value="Option 1")
        self.radio_button = ctk.CTkRadioButton(self, text="Option 1", variable=self.string_var, value="Option 1",
                                               command=self.on_radio_select)
        self.radio_button.grid(row=7, column=0, padx=10, pady=5, columnspan=1, sticky="w")

        self.radio_button = ctk.CTkRadioButton(self, text="Option 2", variable=self.string_var, value="Option 2",
                                               command=self.on_radio_select)
        self.radio_button.grid(row=8, column=0, padx=10, pady=5, columnspan=1, sticky="w")

        self.boolean_var = ctk.BooleanVar()
        self.checkbox = ctk.CTkCheckBox(self, text="Check me", variable=self.boolean_var,
                                        command=self.on_checkbox_toggle)
        self.checkbox.grid(row=9, column=0, padx=10, pady=5, columnspan=1, sticky="w")

        style.create_text(self, 54, 12, 'grey',
                          10, 0, 5, 10, 1, 'n')

        self.progress_value = 0
        self.progress_running = False

    def change_appearance_mode(self, mode):
        ctk.set_appearance_mode(mode)

    def on_button_click(self):
        CTkMessagebox(title="Button Clicked", message="You clicked the button!", icon="check")

    def on_slider_change(self, value):
        print(f"Slider: {value}")

    def on_switch_toggle(self):
        print(f"Switch: {self.switch.get()}")

    def on_radio_select(self):
        print(f"RadioButton: {self.string_var.get()}")

    def on_checkbox_toggle(self):
        print(f"Checkbox: {'checked' if self.boolean_var.get() else 'unchecked'}")

    def start_progress(self):
        self.progress_running = True
        self.update_progress()

    def stop_progress(self):
        self.progress_running = False

    def update_progress(self):
        if self.progress_running:
            self.progress_value += 0.01
            if self.progress_value > 1:
                self.progress_value = 0
            self.progress_bar.set(self.progress_value)
            self.after(50, self.update_progress)

if __name__ == "__main__":
    app = CustomTkinterGuide()
    app.mainloop()
