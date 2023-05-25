import tkinter
import sys

window = tkinter.Tk()

window.title("TEST")
window.attributes("-fullscreen", True)
window['bg'] = '#FFFFFF'

def click():
    window.destroy()
    import page1

def exitApp(event):
    sys.exit()

button = tkinter.Checkbutton(window, text="click", width=15, command=click)
button.pack()

window.bind('<Escape>', exitApp)

window.mainloop()
