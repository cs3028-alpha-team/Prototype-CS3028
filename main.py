from mysql.connector.errors import *
from mysql.connector import *
from business.database_interface import DatabaseInterface
from business.database_populator import DatabasePopulator
from business.mysql_workbench import MySQLWorkbenchInterface

from objects.student import Student

if __name__ == "__main__":
    populator = DatabasePopulator()
    db = DatabaseInterface("alpha_db")

    populator.populate()

    print(" POPULATING DB...\n")

    print("students : ", db.show_table_rows("students"))
    print()
    print("employers : ", db.show_table_rows("employers"))

