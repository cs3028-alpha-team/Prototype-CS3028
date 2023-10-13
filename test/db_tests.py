import unittest

# TODO import classes for db interfaces folder

class DatabaseInterfacesTest(unittest.TestCase):

    pass

    """
    Behaviours to be tested for the MySQLWorkbench interface

    test -> db creation and presence
    - check that database "test_db" doesnt exist before creation
    - check that database "test_db" does exist after calling the create_db method

    test -> db destruction and presence
    - create a database and check that the presence method returns true
    - then call the destroy method and check that the presence method returns false

    Behaviours to be tested for the DatabaseInterface interface

    test -> creation of student and presence
    test -> deletion of student and presence
    test -> creation of employer and presence
    test -> deletion of employer and presence

    """
     

if __name__ == "__main__":
    unittest.main()