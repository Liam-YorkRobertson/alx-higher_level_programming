import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_create_instance(self):
        """
        Test creating an instance of Rectangle with default values.
        """
        r1 = Rectangle(10, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_create_instance_with_arguments(self):
        """
        Test creating an instance of Rectangle with specified values.
        """
        r2 = Rectangle(7, 3, 2, 4, 1)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 1)

    def test_getters_and_setters(self):
        """
        Test the getters and setters of Rectangle class.
        """
        r3 = Rectangle(5, 5)
        r3.width = 8
        r3.height = 12
        r3.x = 2
        r3.y = 3
        self.assertEqual(r3.width, 8)
        self.assertEqual(r3.height, 12)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 3)

    def test_area(self):
        """
        Test calculating the area of a Rectangle.
        """
        r4 = Rectangle(6, 9)
        self.assertEqual(r4.area(), 54)

    def test_str_representation(self):
        """
        Test the string representation of a Rectangle.
        """
        r6 = Rectangle(2, 4, 1, 1, 5)
        expected_output = "[Rectangle] (5) 1/1 - 2/4"
        self.assertEqual(str(r6), expected_output)

    def test_update_args(self):
        """
        Test updating the attributes of a Rectangle using positional arguments.
        """
        r7 = Rectangle(5, 5, 1, 1, 1)
        r7.update(10, 2, 3, 4, 5)
        self.assertEqual(r7.id, 10)
        self.assertEqual(r7.width, 2)
        self.assertEqual(r7.height, 3)
        self.assertEqual(r7.x, 4)
        self.assertEqual(r7.y, 5)

    def test_update_kwargs(self):
        """
        Test updating the attributes of a Rectangle using keyword arguments.
        """
        r8 = Rectangle(5, 5, 1, 1, 1)
        r8.update(id=20, width=8, height=12, x=2, y=3)
        self.assertEqual(r8.id, 20)
        self.assertEqual(r8.width, 8)
        self.assertEqual(r8.height, 12)
        self.assertEqual(r8.x, 2)
        self.assertEqual(r8.y, 3)

    def test_to_dictionary(self):
        """
        Test converting a Rectangle to a dictionary representation.
        """
        r9 = Rectangle(6, 6, 1, 1, 1)
        expected_dict = {'id': 1, 'width': 6, 'height': 6, 'x': 1, 'y': 1}
        self.assertEqual(r9.to_dictionary(), expected_dict)

    def test_save_to_file(self):
        """
        Test saving Rectangle instances to a file in JSON format.
        """
        r10 = Rectangle(3, 3, 0, 0, 1)
        Rectangle.save_to_file([r10])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertIn(str(r10.id), content)
            self.assertIn(str(r10.width), content)
            self.assertIn(str(r10.height), content)
            self.assertIn(str(r10.x), content)
            self.assertIn(str(r10.y), content)

    def test_load_from_file(self):
        """
        Test loading Rectangle instances from a file in JSON format.
        """
        r11 = Rectangle(2, 2, 0, 0, 1)
        Rectangle.save_to_file([r11])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 1)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].id, r11.id)
        self.assertEqual(rectangles[0].width, r11.width)
        self.assertEqual(rectangles[0].height, r11.height)
        self.assertEqual(rectangles[0].x, r11.x)
        self.assertEqual(rectangles[0].y, r11.y)


if __name__ == "__main__":
    unittest.main()
