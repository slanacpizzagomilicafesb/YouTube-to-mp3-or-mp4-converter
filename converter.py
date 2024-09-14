import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.title("Hello World")


def handle_button_press(event):
    window.destroy()

url_entry_frame = tk.Frame()
convert_button_frame = tk.Frame()

url_entry = tk.Entry(master=url_entry_frame,
                     text="Paste URL here...",
                     width=50
                     )
url_entry.pack()

url = url_entry.get()

convert_button = tk.Button(master=convert_button_frame,
                           text="Convert",
                           width=10,
                           height=1
                           )
convert_button.pack()

url_entry_frame.pack()
convert_button_frame.pack()

# Start the event loop.
window.mainloop()