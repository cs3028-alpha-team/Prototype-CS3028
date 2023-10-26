from mysql.connector.errors import *
from mysql.connector import *
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.mysql_workbench import MySQLWorkbenchInterface

from objects.student import Student

if __name__ == "__main__":
    workbench = MySQLWorkbenchInterface()
    #reset database to ensure less errors occur
    workbench.destroy_db("dev_db")
    workbench.create_db("dev_db")

    #set up populator and database
    populator = DatabasePopulator()
    db = DatabaseInterface("dev_db")

    #reset db tables to make sure less errors occur
    print(" RESETTING DB...\n")
    db.reset_table("students")
    db.reset_table("internships")

    #populate database with data passed via csv
    populator.upload_data("students.txt", "internships.txt")

    #display contents of tables in console
    print(" POPULATING DB...\n")
    print("\n - STUDENTS - \n", db.get_table("students"))
    print()
    print("\n - INTERNSHIPS - \n", db.get_table("internships"))

    #dowload data from database tables into csv files
    populator.dowload_data()

