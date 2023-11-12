# Import built-in modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Settings(Frame):

    def __init__(self, func):
        super().__init__()
        # Bridge function connected to main window
        self.func = func
        self.top = Toplevel()
        self.frame = Frame(self.top)
        self.top.title("Matcher Settings")
        self.top.geometry("500x400")

        # Settings variables
        [ self.degree, self.score, self.experience, self.study_mode, self.study_pattern ] = [ IntVar(), IntVar(), IntVar(), IntVar(), IntVar() ]

        Label(
            self.top, 
            text = "Configure matcher settings", 
            bg='#003f88', fg='#ffffff', 
            font = ('Calibri', 12, 'bold')
        ).pack(pady=10)

        # Frame used to position text widgets
        self.text_frame = Frame(self.top)
        self.text_frame.pack(pady=9)
        self.text_frame.configure(bg='#003f88')
        self.top.configure(bg='#003f88')

        # Instructions label
        Label(
            self.text_frame, 
            text = "• Select/deselect criterias and assign them a priority 1 (low) to 5 (high)",  
            bg='#003f88', 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).pack(anchor=W)

        # Define parent frame to position this window's widgets
        self.settings_frame = Frame(self.top)
        self.settings_frame.pack(pady=10)
        self.settings_frame.configure(bg='#003f88')
        self.top.configure(bg='#003f88')

        # -------------------------------------- DEGREE ------------------------------------------

        # Define frame to hold the checkbox and priority dropdown for the 'degree' field
        self.degree_checkbox_frame = Frame(self.settings_frame)
        self.degree_checkbox_frame.configure(bg='#003f88')

        # Configure checkbutton for the 'degree' field
        Checkbutton(
            self.degree_checkbox_frame, 
            text="Degree", 
            variable = self.degree, 
            command = self.toggle_priority_dropdown, 
            onvalue = 1, 
            offvalue = 0, 
            bg='#003f88', 
            activebackground='#003f88', 
            activeforeground='#ffffff', 
            selectcolor='#003f88' , 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).grid(row=0, column=0)

        # Configure priority picker for the 'degree' field
        self.degree_priority_combo = ttk.Combobox(
            self.degree_checkbox_frame, 
            value = ["1", "2", "3", "4", "5"], 
            width=2, 
            state='disabled'
        )
        self.degree_priority_combo.current(0)
        self.degree_priority_combo.grid(row=0, column=1)
        self.degree_checkbox_frame.pack(anchor=W)
        
        # -------------------------------------- SCORE ------------------------------------------

        # Define frame to hold the checkbox and priority dropdown for the 'score' field
        self.score_checkbox_frame = Frame(self.settings_frame)
        self.score_checkbox_frame.configure(bg='#003f88')

        # Configure checkbutton for the 'score' field
        Checkbutton(
            self.score_checkbox_frame, 
            text="Score", 
            variable = self.score, 
            command = self.toggle_priority_dropdown, 
            onvalue = 1, 
            offvalue = 0, 
            bg='#003f88', 
            activebackground='#003f88', 
            activeforeground='#ffffff', 
            selectcolor='#003f88' , 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).grid(row=1, column=0)
        
        # Configure priority picker for the 'score' field
        self.score_priority_combo = ttk.Combobox(
            self.score_checkbox_frame, 
            value = ["1", "2", "3", "4", "5"], 
            width=2, 
            state='disabled'
        )
        self.score_priority_combo.current(0)
        self.score_priority_combo.grid(row=1, column=1)
        self.score_checkbox_frame.pack(anchor=W)

        # -------------------------------------- EXPERIENCE ------------------------------------------

        # Define frame to hold the checkbox and priority dropdown for the 'experience' field
        self.experience_checkbox_frame = Frame(self.settings_frame)
        self.experience_checkbox_frame.configure(bg='#003f88')

        # Configure checkbutton for the 'experience' field
        Checkbutton(
            self.experience_checkbox_frame, 
            text="Experience", 
            variable = self.experience, 
            command = self.toggle_priority_dropdown, 
            onvalue = 1, 
            offvalue = 0, 
            bg='#003f88', 
            activebackground='#003f88', 
            activeforeground='#ffffff', 
            selectcolor='#003f88' , 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).grid(row=2, column=0)
        
        # Configure priority picker for the 'experience' field
        self.experience_priority_combo = ttk.Combobox(
            self.experience_checkbox_frame, 
            value = ["1", "2", "3", "4", "5"], 
            width=2, 
            state='disabled'
        )
        self.experience_priority_combo.current(0)
        self.experience_priority_combo.grid(row=2, column=1)
        self.experience_checkbox_frame.pack(anchor=W)

        # -------------------------------------- STUDY MODE ------------------------------------------

        # Define frame to hold the checkbox and priority dropdown for the 'study mode' field
        self.studymode_checkbox_frame = Frame(self.settings_frame)
        self.studymode_checkbox_frame.configure(bg='#003f88')

        # Configure checkbutton for the 'study mode' field
        Checkbutton(
            self.studymode_checkbox_frame, 
            text="Study mode", 
            variable = self.study_mode, 
            command = self.toggle_priority_dropdown, 
            onvalue = 1, 
            offvalue = 0,
            bg='#003f88', 
            activebackground='#003f88', 
            activeforeground='#ffffff', 
            selectcolor='#003f88' , 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).grid(row=3, column=0)
        
        # Configure priority picker for the 'study mode' field
        self.studymode_priority_combo = ttk.Combobox(
            self.studymode_checkbox_frame, 
            value = ["1", "2", "3", "4", "5"], 
            width=2, 
            state='disabled'
        )
        self.studymode_priority_combo.current(0)
        self.studymode_priority_combo.grid(row=3, column=1)
        self.studymode_checkbox_frame.pack(anchor=W)

        # -------------------------------------- STUDY PATTERN ------------------------------------------

        # Define frame to hold the checkbox and priority dropdown for the 'study pattern' field
        self.studypattern_checkbox_frame = Frame(self.settings_frame)
        self.studypattern_checkbox_frame.configure(bg='#003f88')

        # Configure checkbutton for the 'study mode' field
        Checkbutton(
            self.studypattern_checkbox_frame, 
            text="Study pattern", 
            variable = self.study_pattern, 
            command = self.toggle_priority_dropdown, 
            onvalue = 1, 
            offvalue = 0,
            bg='#003f88', 
            activebackground='#003f88', 
            activeforeground='#ffffff', 
            selectcolor='#003f88' , 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).grid(row=3, column=0)
        
        # Configure priority picker for the 'study mode' field
        self.studypattern_priority_combo = ttk.Combobox(
            self.studypattern_checkbox_frame, 
            value = ["1", "2", "3", "4", "5"], 
            width=2, 
            state='disabled'
        )
        self.studypattern_priority_combo.current(0)
        self.studypattern_priority_combo.grid(row=3, column=1)
        self.studypattern_checkbox_frame.pack(anchor=W)

        # Button responsible for sending 'settings' object back to main window
        Button(self.settings_frame, 
            text = 'Apply & Match', 
            font = ('Calibri', 12, 'bold'), 
            width=15, 
            fg='#003f88', 
            activeforeground='#003f88', 
            activebackground='#f1a13b', 
            bg='#fdc500', 
            relief=FLAT, 
            command = self.send_data
        ).pack(anchor=W, pady=15)

    # -------------------------------------- AUXILIARY FUNCTIONS ------------------------------------------

    # Transfer settings back to the parent window
    def send_data(self):

        # Collect settings values at timestamp where send_date was invoked
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

        # Invoke the bridge function and destroy the settings window
        self.func(settings)
        self.top.destroy()

    # For each dropdown, allow selection only if corresponding checkbox is selected
    def toggle_priority_dropdown(self):
        self.degree_priority_combo.config(state = 'normal' if self.degree.get() == 1 else 'disabled')
        self.score_priority_combo.config(state = 'normal' if self.score.get() == 1 else 'disabled')
        self.experience_priority_combo.config(state = 'normal' if self.experience.get() == 1 else 'disabled')
        self.studymode_priority_combo.config(state = 'normal' if self.study_mode.get() == 1 else 'disabled')
        self.studypattern_priority_combo.config(state = 'normal' if self.study_pattern.get() == 1 else 'disabled')