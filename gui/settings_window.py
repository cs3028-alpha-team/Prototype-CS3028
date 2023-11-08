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
        self.top.geometry("800x400")

        # Settings to be applied 
        self.degree = IntVar()
        self.score = IntVar()
        self.experience = IntVar()
        self.study_mode = IntVar()
        self.study_pattern = IntVar()

        Label(self.top, text = "Configure matcher settings", bg='#003f88', fg='#ffffff', font = ('Calibri', 12, 'bold')).pack(pady=10)

        # frame to position text widgets
        self.text_frame = Frame(self.top)
        self.text_frame.pack(pady=9)
        self.text_frame.configure(bg='#003f88')
        self.top.configure(bg='#003f88')

        Label(self.text_frame, text = "• Select/deselect criterias and assign them a priority 1 (low) to 5 (high)",  bg='#003f88', fg='#ffffff', font = ('Calibri', 12)).pack(anchor=W)
        Label(self.text_frame, text = "• Student score will be selected by default ", bg='#003f88', fg='#ffffff', font = ('Calibri', 12)).pack(anchor=W)
        Label(self.text_frame, text = "• If not all fields ticked are assigned a priority they will default to 1", bg='#003f88', fg='#ffffff', font = ('Calibri', 12)).pack(anchor=W)

        # frame to position settings picker
        self.settings_frame = Frame(self.top)
        self.settings_frame.pack(pady=9)
        self.settings_frame.configure(bg='#003f88')
        self.top.configure(bg='#003f88')

        # settings pickers 
        Checkbutton(self.settings_frame, text="Degree", variable = self.degree, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row= 0, column=0)
        Checkbutton(self.settings_frame, text="Score", variable = self.score, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row= 1, column=0)
        Checkbutton(self.settings_frame, text="Experience", variable = self.experience, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row= 2, column=0)
        Checkbutton(self.settings_frame, text="Study mode", variable = self.study_mode, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row= 3, column=0)
        Checkbutton(self.settings_frame, text="Study pattern", variable = self.study_pattern, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row= 4, column=0)

        # store settings
        self.settings = {
            'origin' : 'settings',
        }

    # transfer settings back to the parent window
    def send_data(self):
        self.func(self.settings)
        self.top.destroy()