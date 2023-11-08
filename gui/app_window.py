from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import sys
sys.path.append("../")
from objects.student import Student
from objects.internship import Internship
from business.matcher import Matcher
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.mysql_workbench import MySQLWorkbenchInterface

class AppWindow(Tk):
    def __init__(self):
        super().__init__()
        self.workbench = MySQLWorkbenchInterface()
        self.matcher = Matcher()
            
        # Reset database to ensure fewer errors occur
        self.workbench.destroy_db("alpha_db")
        self.workbench.create_db("alpha_db")

        # Set up populator and database
        self.populator = DatabasePopulator()
        self.db = DatabaseInterface("alpha_db")

        # Reset database tables to make sure fewer errors occur
        self.db.reset_table("students")
        self.db.reset_table("internships")

        # Populate database with data passed via CSV
        students_input = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\studentsdata.csv'
        internships_input = 'C:\\Users\\matti\\OneDrive\\Desktop\\CS3028 Project\\mysql-interface\\inputs\\internshipsdata.csv'
        self.populator.populate_via_csv(students_input, internships_input)

        self.title("CS3028 Team Alpha")
        self.geometry("500x350")
        self.resizable(False, False)
        self.configure(bg='#003f88')

        # frame used to position widgets on this window
        self.buttons_frame = Frame(self)
        self.buttons_frame.configure(bg='#003f88')

        # variable deciding whether output printed to console
        self.print_output = IntVar()

        Label(self, text = 'Internship Matchmaker', font = ('Calibri', 15, 'bold'), fg='#ffffff', bg='#003f88').pack(pady=15)
        Label(self, text = "Run matcher, or configure custom matcher settings.\n Results will be automatically stored in 'matches.csv'", bg='#003f88', fg='#ffffff', font = ('Calibri', 12)).pack(pady=10, padx=15)
        Button(self.buttons_frame, text = 'Run Match', font = ('Calibri', 12, 'bold'), width=12, fg='#003f88', activeforeground='#003f88', activebackground='#f1a13b', bg='#fdc500', relief=FLAT, command = self.default_matcher).pack(fill= BOTH, expand= True, pady= 10)
        Button(self.buttons_frame, text = 'Settings', font = ('Calibri', 12, 'bold'), width=12, fg='#003f88', activeforeground='#003f88', activebackground='#f1a13b', bg='#fdc500', relief=FLAT, command = self.configure_matcher).pack(fill= BOTH, expand= True, pady= 10)
        
        # add radio button to print to terminal
        Checkbutton(self.buttons_frame, text="Print results to console", variable = self.print_output, onvalue = 1, offvalue = 0, bg='#003f88', activebackground='#003f88', activeforeground='#ffffff', selectcolor='#003f88' , fg='#ffffff', font = ('Calibri', 12)).pack(anchor=W, pady=10)

        self.buttons_frame.pack()
        self.mainloop()

    def default_matcher(self):
        # Fetch students and internships from the database
        student_records = self.db.get_table("students")
        internship_records = self.db.get_table("internships")

        # Create instances of Student and Internship from the fetched records
        students = [Student(record[0], record[2], record[3], record[4], record[5], record[6]) for record in student_records]
        internships = [Internship(record[0], record[2], record[3], record[4]) for record in internship_records]

        # Match students with internships and save matches to csv
        matches, unmatched = self.matcher.filter_matches(students, internships)

        if self.print_output.get() == 1:
            print("Matched students : ")
            # Print stringified matches 
            for (student, internship) in matches.items():
                print(f"{student.get_fullname()} matched for {internship.get_title()} at {internship.get_organization()}")
            print("\nUnmatched students : ")
            # Print names of unmatched students
            for student in unmatched:
                print(student.get_fullname())

    def configure_matcher(self):
        pass
