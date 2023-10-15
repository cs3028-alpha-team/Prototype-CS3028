import unittest
import sys

sys.path.append("./")
from business.db_interfaces import MySQLWorkbenchInterface

class MySQLWorkbenchInterfaceTest(unittest.TestCase):

    # test create_db method and db_exists method
    def test_db_creation(self):
        workbench = MySQLWorkbenchInterface()
        workbench.create_db("test_db")
        self.assertEqual(workbench.db_exists("test_db"), True)

    # test destroy_db method and db_exists method
    def test_db_destruction(self):
        workbench = MySQLWorkbenchInterface()
        workbench.destroy_db("test_db")
        self.assertEqual(workbench.db_exists("test_db"), False)


if __name__ == "__main__":
    unittest.main()