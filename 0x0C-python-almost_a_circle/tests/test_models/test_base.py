import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_instance_with_id(self):
        """
        Test creating an instance of Base with a specific ID.
        """
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_create_instance_without_id(self):
        """
        Test creating instances of Base without specifying ID.
        """
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)

    def test_create_instance_with_negative_id(self):
        """
        Test creating an instance of Base with a negative ID.
        """
        base = Base(-10)
        self.assertEqual(base.id, -10)

    def test_create_instance_with_zero_id(self):
        """
        Test creating an instance of Base with zero as the ID.
        """
        base = Base(0)
        self.assertEqual(base.id, 0)

    def test_create_instance_with_float_id(self):
        """
        Test creating an instance of Base with a float ID.
        """
        base = Base(3.14)
        self.assertEqual(base.id, 3.14)

    def test_create_instance_with_string_id(self):
        """
        Test creating an instance of Base with a string ID.
        """
        base = Base("abc")
        self.assertEqual(base.id, "abc")

    def test_create_instance_with_none_id(self):
        """
        Test creating an instance of Base with None as the ID.
        """
        base = Base(None)
        self.assertIsNotNone(base.id)

    def test_create_multiple_instances(self):
        """
        Test creating multiple instances of Base.
        """
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base2.id, base3.id)
        self.assertNotEqual(base3.id, base1.id)

    def test_to_json_string(self):
        """
        Test converting a list of Base instances to JSON string.
        """
        base = Base(1)
        json_str = Base.to_json_string([base.__dict__])
        self.assertEqual(json_str, '[{"id": 1}]')


if __name__ == '__main__':
    unittest.main()
