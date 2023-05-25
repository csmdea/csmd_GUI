import tkinter as tk
from tkinter import ttk

def open_page2():
    subprocess.Popen(["python", "page2.py"])
    window.destroy()

window = tk.Tk()

style = ttk.Style()
style.configure("Custom.TButton",
                foreground="white",
                background="blue",
                font=("Arial", 12),
                padding=10)

button = ttk.Button(window, text="화면 전환", style="Custom.TButton", command=open_page2)
button.pack()

window.mainloop()
