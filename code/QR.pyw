from tkinter import *
from tkinter.ttk import *
import pyqrcode as pqr
import png
import io

def qr():
    url = pqr.create("%s"% first_input.get())
    with open('%s.png'% second_input.get(), 'w') as fstream:
        url.png('%s.png'% second_input.get(), scale=10)
    buffer = io.BytesIO()
    url.png(buffer)

window = Tk()
window.title("QR CODE GENERATOR")
window.geometry('400x160')
window.configure(background="#ededed")
window.resizable(width=False, height=False)

first_title = Label(window, text='Insira o link que deseja converter',background="#ededed", foreground="#000", anchor = N)
first_title.place(x=0, y=10, width=400, height=25)
first_title.configure(font=('Segoe UI', 12))

first_input = Entry(window)
first_input.place(x=25, y=35, width=350)

second_title = Label(window, text='Insira o nome que deseja salvar o arquivo',background="#ededed", foreground="#000", anchor = N)
second_title.place(x=0, y=60, width=400, height=25)
second_title.configure(font=('Segoe UI', 12))

second_input = Entry(window)
second_input.place(x=25, y=85, width=350)

btn = Button(window, text='Gerar', command=qr)
btn.place(x=25, y=120, width=350)

footer = Label(window, text='by Marcus Vinícius Augusto Rocha', background="#ededed", foreground="#000", anchor=N)
footer.place(x=280, y=145, width=115)
footer.configure(font=('Segoe UI', 5))

window.mainloop()
