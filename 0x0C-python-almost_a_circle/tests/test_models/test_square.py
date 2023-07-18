import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_create_instance(self):
        """
        Test creating an instance of Square with default values.
        """
        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

    def test_create_instance_with_arguments(self):
        """
        Test creating an instance of Square with specified values.
        """
        s2 = Square(5, 2, 3, 10)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 10)

    def test_getters_and_setters(self):
        """
        Test the getters and setters of Square class.
        """
        s3 = Square(3)
        self.assertEqual(s3.size, 3)
        s3.size = 8
        self.assertEqual(s3.size, 8)

    def test_str_representation(self):
        """
        Test the string representation of a Square.
        """
        s4 = Square(4, 1, 2, 20)
        self.assertEqual(str(s4), "[Square] (20) 1/2 - 4")

    def test_update_args(self):
        """
        Test updating the attributes of a Square using positional arguments.
        """
        s5 = Square(3)
        s5.update(1, 5, 2, 3)
        self.assertEqual(s5.id, 1)
        self.assertEqual(s5.size, 5)
        self.assertEqual(s5.x, 2)
        self.assertEqual(s5.y, 3)

    def test_update_kwargs(self):
        """
        Test updating the attributes of a Square using keyword arguments.
        """
        s6 = Square(2)
        s6.update(id=2, size=4, x=1, y=2)
        self.assertEqual(s6.id, 2)
        self.assertEqual(s6.size, 4)
        self.assertEqual(s6.x, 1)
        self.assertEqual(s6.y, 2)

    def test_to_dictionary(self):
        """
        Test converting a Square to a dictionary representation.
        """
        s7 = Square(3, 1, 2, 30)
        expected_dict = {'id': 30, 'size': 3, 'x': 1, 'y': 2}
        self.assertDictEqual(s7.to_dictionary(), expected_dict)

    def test_area(self):
        """
        Test calculating the area of a Square.
        """
        s8 = Square(4)
        self.assertEqual(s8.area(), 16)

    def test_from_dictionary(self):
        """
        Test creating a Square instance from a dictionary.
        """
        dictionary = {'id': 10, 'size': 5, 'x': 2, 'y': 1}
        s10 = Square(**dictionary)
        self.assertEqual(s10.id, 10)
        self.assertEqual(s10.size, 5)
        self.assertEqual(s10.x, 2)
        self.assertEqual(s10.y, 1)

if __name__ == "__main__":
    unittest.main()
