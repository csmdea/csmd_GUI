import tkinter

window=tkinter.Tk()

window.title("TEST")
window.geometry("1240x1240+100+100")
window.resizable(False, False)

window['bg'] = '#FFFFFF'

count=0

def countUP():
    global count
    count +=1
    label.config(text=str(count))

label=tkinter.Label(window, text="파이썬", width=10, height=5, fg="red", relief="solid")
label.pack()

button = tkinter.Button(window, text="click",overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()
