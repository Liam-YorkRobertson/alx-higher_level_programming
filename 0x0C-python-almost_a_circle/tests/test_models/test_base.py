import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_type(self):
        """
        Test if the ID attribute is of integer type.
        """
        obj = Base()
        self.assertIsInstance(obj.id, int)

    def test_id_assignment(self):
        """
        Test if IDs are assigned correctly to instances of the Base class.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_argument(self):
        """
        Test if the ID is correctly assigned when a specific ID is passed as an argument.
        """
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_id_increment(self):
        """
        Test if the ID is incremented for each new instance of the Base class.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj2.id - obj1.id, 1)

    def test_multiple_instances(self):
        """
        Test if multiple instances of the Base class maintain separate ID counts.
        """
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_id_argument_edge_case(self):
        """
        Test if passing a negative ID as an argument results in correct assignment.
        """
        obj = Base(-10)
        self.assertEqual(obj.id, -10)


if __name__ == "__main__":
    unittest.main()
