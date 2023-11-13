# Import built-in modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys

# Import required classes
sys.path.append("../")
from objects.student import Student
from objects.internship import Internship
from business.matcher import Matcher
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.mysql_workbench import MySQLWorkbenchInterface
from .settings_window import Settings

class AppWindow(Tk):

    def __init__(self):
        super().__init__()
        # Set up interfaces defined in 'business' folder
        self.workbench = MySQLWorkbenchInterface()
        self.matcher = Matcher()
            
        # Reset database to ensure fewer errors occur
        self.workbench.destroy_db("alpha_db")
        self.workbench.create_db("alpha_db")

        # Set up populator and database interfaces
        self.populator = DatabasePopulator()
        self.db = DatabaseInterface("alpha_db")

        # Reset database tables to make sure fewer errors occur
        self.db.reset_table("students")
        self.db.reset_table("internships")

        # Populate database with data passed via CSV
        students_input = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\studentsdata.csv'
        internships_input = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\internshipsdata.csv'
        self.populator.populate_via_csv(students_input, internships_input)

        # Configure window appearance
        self.title("CS3028 Team Alpha")
        self.geometry("500x300")
        self.resizable(False, False)
        self.configure(bg='#003f88')
        self.resizable(False, False)

        # Frame used to position widgets on this window
        self.buttons_frame = Frame(self)
        self.buttons_frame.configure(bg='#003f88')

        # Variable to determine whether output printed to console
        self.print_output = IntVar()

        # Instruction for use labels
        Label(
            self, 
            text = 'Internship Matchmaker', 
            font = ('Calibri', 15, 'bold'), 
            fg='#ffffff', 
            bg='#003f88'
        ).pack(pady=15)

        Label(
            self, 
            text = "Run matcher, or configure custom matcher settings.\n Results will be automatically stored in 'matches.csv'", 
            bg='#003f88', 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).pack(pady=10, padx=15)

        # Button to run default matching algorithm
        Button(
            self.buttons_frame, 
            text = 'Run Match', 
            font = ('Calibri', 12, 'bold'), 
            width=12, 
            fg='#003f88', 
            activeforeground='#003f88', 
            activebackground='#f1a13b', 
            bg='#fdc500', 
            relief=FLAT, 
            command = self.run_default_matcher
        ).pack(fill= BOTH, expand= True, pady= 10)

        # Button to configure custom settings for matching algorithm
        Button(
            self.buttons_frame, 
            text = 'Settings', 
            font = ('Calibri', 12, 'bold'), 
            width=12, 
            fg='#003f88', 
            activeforeground='#003f88', 
            activebackground='#f1a13b', 
            bg='#fdc500', 
            relief=FLAT, 
            command = self.configure_settings
        ).pack(fill= BOTH, expand= True, pady= 10)
        
        # Checkbutton to display matching results to terminal in addition to writing them to 'matches.csv'
        Checkbutton(
            self.buttons_frame, 
            text="Print results to console", 
            variable = self.print_output, 
            onvalue = 1, 
            offvalue = 0, 
            bg='#003f88', 
            activebackground='#003f88', 
            activeforeground='#ffffff', 
            selectcolor='#003f88' , 
            fg='#ffffff', 
            font = ('Calibri', 12)
        ).pack(anchor=W, pady=10)

        self.buttons_frame.pack()
        self.mainloop()

    # Run the default matching algorithm, where all fields have equal priority
    def run_default_matcher(self):
        # Fetch students and internships from the database
        student_records = self.db.get_table("students")
        internship_records = self.db.get_table("internships")

        # Create instances of Student and Internship from the fetched records
        students = [Student(record[0], record[2], record[3], record[4], record[5], record[6]) for record in student_records]
        internships = [Internship(record[0], record[2], record[3], record[4]) for record in internship_records]

        # Match students with internships and save matches to csv
        matches, unmatched = self.matcher.filter_matches(students, internships)

        # Print results of matching algorithm to terminal, if checkbox was ticked
        if self.print_output.get() == 1:
            print("Matched students : ")
            for (student, internship) in matches.items():
                print(f"{student.get_fullname()} matched for {internship.get_title()} at {internship.get_organization()}")
            print("\nUnmatched students : ")
            for student in unmatched:
                print(student.get_fullname())

    # Invoke the 'settings' window
    def configure_settings(self):
        Settings(self.run_custom_matcher)

    # Run custom matching algorithm by applying user settings
    def run_custom_matcher(self, settings):
        print("\nCustom settings to be applied : ")
        print(settings)
        # TODO : implement custom matching algorithm