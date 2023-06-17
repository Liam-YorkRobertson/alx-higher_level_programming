import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_width_assignment(self):
        """
        Test if the width attribute is assigned correctly.
        """
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.width, 10)

    def test_height_assignment(self):
        """
        Test if the height attribute is assigned correctly.
        """
        rectangle = Rectangle(10, 5)
        self.assertEqual(rectangle.height, 5)

    def test_x_assignment(self):
        """
        Test if the x attribute is assigned correctly.
        """
        rectangle = Rectangle(10, 5, 2)
        self.assertEqual(rectangle.x, 2)

    def test_y_assignment(self):
        """
        Test if the y attribute is assigned correctly.
        """
        rectangle = Rectangle(10, 5, 2, 3)
        self.assertEqual(rectangle.y, 10)

    def test_id_assignment(self):
        """
        Test if the id attribute is assigned correctly.
        """
        rectangle = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(rectangle.id, 1)

    def test_width_type(self):
        """
        Test if the width attribute is of integer type.
        """
        rectangle = Rectangle(10, 5)
        self.assertIsInstance(rectangle.width, int)

    def test_height_type(self):
        """
        Test if the height attribute is of integer type.
        """
        rectangle = Rectangle(10, 5)
        self.assertIsInstance(rectangle.height, int)

    def test_x_type(self):
        """
        Test if the x attribute is of integer type.
        """
        rectangle = Rectangle(10, 5, 2)
        self.assertIsInstance(rectangle.x, int)

    def test_y_type(self):
        """
        Test if the y attribute is of integer type.
        """
        rectangle = Rectangle(10, 5, 2, 3)
        self.assertIsInstance(rectangle.y, int)


if __name__ == "__main__":
    unittest.main()
