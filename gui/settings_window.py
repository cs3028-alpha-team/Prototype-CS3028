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
        self.top.geometry("500x400")

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
        self.settings_frame.pack(pady=10)
        self.settings_frame.configure(bg='#003f88')
        self.top.configure(bg='#003f88')

        # settings pickers 

        # 1. Degree checkbox and priority picker
        self.degree_checkbox_frame = Frame(self.settings_frame)
        self.degree_checkbox_frame.configure(bg='#003f88')
        self.degree_checkbox_frame.columnconfigure(0, weight=1)

        Checkbutton(self.degree_checkbox_frame, text="Degree", variable = self.degree, command = self.toggle_priority_dropdown, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row=0, column=0)
        self.degree_priority_combo = ttk.Combobox(self.degree_checkbox_frame, value = ["1", "2", "3", "4", "5"], width=2, state='disabled')
        self.degree_priority_combo.current(0)
        self.degree_priority_combo.grid(row=0, column=1)
        self.degree_checkbox_frame.pack(anchor=W)
        
        # 2. Score checkbox and priority picker
        self.score_checkbox_frame = Frame(self.settings_frame)
        self.score_checkbox_frame.configure(bg='#003f88')
        Checkbutton(self.score_checkbox_frame, text="Score", variable = self.score, command = self.toggle_priority_dropdown, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row=1, column=0)
        self.score_priority_combo = ttk.Combobox(self.score_checkbox_frame, value = ["1", "2", "3", "4", "5"], width=2, state='disabled')
        self.score_priority_combo.current(0)
        self.score_priority_combo.grid(row=1, column=1)
        self.score_checkbox_frame.pack(anchor=W)

        # 3. Experience checkbox and priority picker
        self.experience_checkbox_frame = Frame(self.settings_frame)
        Checkbutton(self.experience_checkbox_frame, text="Experience", variable = self.experience, command = self.toggle_priority_dropdown, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row=2, column=0)
        self.experience_priority_combo = ttk.Combobox(self.experience_checkbox_frame, value = ["1", "2", "3", "4", "5"], width=2, state='disabled')
        self.experience_priority_combo.current(0)
        self.experience_priority_combo.grid(row=2, column=1)
        self.experience_checkbox_frame.configure(bg='#003f88')
        self.experience_checkbox_frame.pack(anchor=W)

        # 4. Study mode checkbox and priority picker
        self.studymode_checkbox_frame = Frame(self.settings_frame)
        Checkbutton(self.studymode_checkbox_frame, text="Study mode", variable = self.study_mode, command = self.toggle_priority_dropdown, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row=3, column=0)
        self.studymode_priority_combo = ttk.Combobox(self.studymode_checkbox_frame, value = ["1", "2", "3", "4", "5"], width=2, state='disabled')
        self.studymode_priority_combo.current(0)
        self.studymode_priority_combo.grid(row=3, column=1)
        self.studymode_checkbox_frame.configure(bg='#003f88')
        self.studymode_checkbox_frame.pack(anchor=W)

        # 5. Study pattern checkbox and priority picker
        self.studypattern_checkbox_frame = Frame(self.settings_frame)
        Checkbutton(self.studypattern_checkbox_frame, text="Study pattern", variable = self.study_pattern, command = self.toggle_priority_dropdown, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).grid(row=4, column=0)      
        self.studypattern_priority_combo = ttk.Combobox(self.studypattern_checkbox_frame, value = ["1", "2", "3", "4", "5"], width=2, state='disabled')
        self.studypattern_priority_combo.current(0)
        self.studypattern_priority_combo.grid(row=4, column=1)
        self.studypattern_checkbox_frame.configure(bg='#003f88')
        self.studypattern_checkbox_frame.pack(anchor=W)

        # Button to send settings packet back to main window
        Button(self.settings_frame, text = 'Apply & Match', font = ('Calibri', 12, 'bold'), width=15, fg='#003f88', activeforeground='#003f88', activebackground='#f1a13b', bg='#fdc500', relief=FLAT, command = self.send_data).pack(anchor=W, pady=15)

    # transfer settings back to the parent window
    def send_data(self):

        # store settings
        settings = {
            'origin' : 'settings',
            'degree' : {
                'selected' : self.degree.get(),
                'priority' : self.degree_priority_combo.get()
            },
            'score' : {
                'selected' : self.score.get(),
                'priority' : self.score_priority_combo.get()
            },
            'experience' : {
                'selected' : self.experience.get(),
                'priority' : self.experience_priority_combo.get()
            },
            'study_mode' : {
                'selected' : self.study_mode.get(),
                'priority' : self.studymode_priority_combo.get()
            },
            'study_pattern' : {
                'selected' : self.study_pattern.get(),
                'priority' : self.studypattern_priority_combo.get()
            }
        }

        self.func(settings)
        self.top.destroy()

    #for each dropdown, allow selection only if corresponding checkbox is selected
    def toggle_priority_dropdown(self):
        # Degree 
        self.degree_priority_combo.config(state = 'normal' if self.degree.get() == 1 else 'disabled')
        # Score
        self.score_priority_combo.config(state = 'normal' if self.score.get() == 1 else 'disabled')
        # Experience
        self.experience_priority_combo.config(state = 'normal' if self.experience.get() == 1 else 'disabled')
        # Study mode
        self.studymode_priority_combo.config(state = 'normal' if self.study_mode.get() == 1 else 'disabled')
        # Study pattern
        self.studypattern_priority_combo.config(state = 'normal' if self.study_pattern.get() == 1 else 'disabled')
