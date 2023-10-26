from mysql.connector.errors import *
from mysql.connector import *
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.mysql_workbench import MySQLWorkbenchInterface

from objects.student import Student

if __name__ == "__main__":
    workbench = MySQLWorkbenchInterface()

    workbench.destroy_db("dev_db")

    workbench.create_db("dev_db")

    populator = DatabasePopulator()
    db = DatabaseInterface("dev_db")

    print(" RESETTING DB...\n")

    db.reset_table("students")
    db.reset_table("internships")

    populator.populate_via_csv("students.txt", "internships.txt")

    print(" POPULATING DB...\n")

    print("\n - STUDENTS - \n", db.show_table_rows("students"))
    print()
    print("\n - INTERNSHIPS - \n", db.show_table_rows("internships"))

