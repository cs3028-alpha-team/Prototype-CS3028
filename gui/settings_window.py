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
        self.top.geometry("500x350")
        self.top.resizable(False, False)

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
            text = "Toggle criteria selection by ticking the checkboxes\nAssign each criteria a priority using the dropdowns",  
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

        # Configure checkbutton for the 'degree' field
        Checkbutton(
            self.settings_frame, 
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
        ).grid(row=0, column=0, sticky="w", padx=10)

        # Configure priority picker for the 'degree' field
        self.degree_priority_combo = ttk.Combobox(
            self.settings_frame, 
            values = [1], 
            width=2, 
            state='disabled'
        )
        self.degree_priority_combo.current(0)
        self.degree_priority_combo.grid(row=0, column=1)
        
        # -------------------------------------- SCORE ------------------------------------------

        # Configure checkbutton for the 'score' field
        Checkbutton(
            self.settings_frame, 
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
        ).grid(row=1, column=0, sticky="w", padx=10)
        
        # Configure priority picker for the 'score' field
        self.score_priority_combo = ttk.Combobox(
            self.settings_frame, 
            values = [1], 
            width=2, 
            state='disabled'
        )
        self.score_priority_combo.current(0)
        self.score_priority_combo.grid(row=1, column=1)

        # -------------------------------------- EXPERIENCE ------------------------------------------

        # Configure checkbutton for the 'experience' field
        Checkbutton(
            self.settings_frame, 
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
        ).grid(row=2, column=0, sticky="w", padx=10)
        
        # Configure priority picker for the 'experience' field
        self.experience_priority_combo = ttk.Combobox(
            self.settings_frame, 
            values = [1], 
            width=2, 
            state='disabled'
        )
        self.experience_priority_combo.current(0)
        self.experience_priority_combo.grid(row=2, column=1)

        # -------------------------------------- STUDY MODE ------------------------------------------

        # Configure checkbutton for the 'study mode' field
        Checkbutton(
            self.settings_frame, 
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
        ).grid(row=3, column=0, sticky="w", padx=10)
        
        # Configure priority picker for the 'study mode' field
        self.studymode_priority_combo = ttk.Combobox(
            self.settings_frame, 
            values = [1], 
            width=2, 
            state='disabled'
        )
        self.studymode_priority_combo.current(0)
        self.studymode_priority_combo.grid(row=3, column=1)

        # -------------------------------------- STUDY PATTERN ------------------------------------------

        # Configure checkbutton for the 'study mode' field
        Checkbutton(
            self.settings_frame, 
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
        ).grid(row=4, column=0, sticky="w", padx=10)
        
        # Configure priority picker for the 'study mode' field
        self.studypattern_priority_combo = ttk.Combobox(
            self.settings_frame, 
            values = [1], 
            width=2, 
            state='disabled'
        )
        self.studypattern_priority_combo.current(0)
        self.studypattern_priority_combo.grid(row=4, column=1)

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
        ).grid(row=5, column=0, columnspan=2, pady=15)

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

        # Toggle the state of each checkbox
        self.degree_priority_combo.config(state = 'normal' if self.degree.get() == 1 else 'disabled')
        self.score_priority_combo.config(state = 'normal' if self.score.get() == 1 else 'disabled')
        self.experience_priority_combo.config(state = 'normal' if self.experience.get() == 1 else 'disabled')
        self.studymode_priority_combo.config(state = 'normal' if self.study_mode.get() == 1 else 'disabled')
        self.studypattern_priority_combo.config(state = 'normal' if self.study_pattern.get() == 1 else 'disabled')

        # Update the priority options for each dropdown
        self.degree_priority_combo['values'] = self.compute_priorities()
        self.score_priority_combo['values'] = self.compute_priorities()
        self.experience_priority_combo['values'] = self.compute_priorities()
        self.studymode_priority_combo['values'] = self.compute_priorities()
        self.studypattern_priority_combo['values'] = self.compute_priorities()

    # Compute available priorities for each dropdown combobox
    def compute_priorities(self):
        total = 1 + self.degree.get() + self.score.get() + self.experience.get() + self.study_mode.get() + self.study_pattern.get()
        priorities = [ i for i in range(1, total) ]
        return priorities

        # now check which checkboxes are checked and get the value selected
        # then remove that value from the array to be returned
        # if it doesnt work then use function binding