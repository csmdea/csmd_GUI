import tkinter
import sys

window = tkinter.Tk()

window.title("PAGE1")
window.attributes("-fullscreen", True)
window['bg'] = '#FFFFFF'

count = 0

def countUP():
    global count
    count += 1
    label.config(text=str(count))

def exitApp(event):
    sys.exit()

label = tkinter.Label(window, text="파이썬", width=10, height=5, fg="red", relief="solid")
label.pack()

button = tkinter.Checkbutton(window, text="click", overrelief="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()


# 'ESC' 키를 눌렀을 때 exitApp 함수가 호출되도록 바인딩합니다.
window.bind('<Escape>', exitApp)

window.mainloop()
