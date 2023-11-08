from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Settings(Frame):
    def __init__(self, func):
        super().__init__()
        self.func = func # allows data to be send to the window which invoked the current one
        self.top = Toplevel()
        self.frame = Frame(self.top)
        self.top.title("Matcher Settings")
        self.top.geometry("400x400")

        # Settings to be applied 
        self.x = StringVar()

        #Label(self.top, text = "Fill-in the fields below with your credentials", bg='#003f88', fg='#ffffff', font = ('Calibri', 12, 'bold')).pack(pady=10)

        # frame to position window widgets
        self.f = Frame(self.top)
        self.f.pack(pady=9)
        self.f.configure(bg='#003f88')
        self.top.configure(bg='#003f88')
        
        Label(self.f, text='Username', bg='#003f88', fg='#ffffff', font=('Calibri',12,'bold')).grid(row=0, column=0, padx=5)
        Entry(self.f, textvariable=self.x).grid(row=0, column=1)
        # Label(self.f, text='Password', bg='#003f88', fg='#ffffff', font=('Calibri',12,'bold')).grid(row=1, column=0, padx=5)
        # Entry(self.f, textvariable=self.password, show="*").grid(row=1, column=1)
        Button(self.top, text='Submit',font=('Calibri', 12, 'bold'), width=10, fg='#003f88', activeforeground='#003f88', bg='#fdc500', activebackground='#f1a13b', relief=FLAT, command=self.send_data).pack(pady=10)

        # store the origin of the form data 
        self.settings = {
            'origin' : 'settings',
            'x' : self.x,
        }

    def send_data(self):
        self.func(self.settings)
        self.top.destroy()