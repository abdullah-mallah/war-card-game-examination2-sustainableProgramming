"""
This script is used to test class FileRW.

Authors: Abdullah Mallah, Eszter Kalmar and Hampus Gunnarsson.
"""

import unittest
from file_reader_writer import FileRW


class TestFileReaderWriter(unittest.TestCase):
    """Responsible for tests of class FileRW."""

    def setUp(self) -> None:
        """Create objects before each test method."""
        self.frw = FileRW('score.txt')

    def test_check_name(self):
        """
        Test the method to check if player exist in text file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [["a", "0", "0", "0.0"]]
        self.frw.store_names(name_list)
        self.assertEqual(self.frw.check_name("a"), True)
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.check_name("a")

    def test_store_names(self):
        """
        Test the method to check if player's information stored in txt file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [["a", "0", "0", "0.0"]]
        self.frw.store_names(name_list)
        self.assertEqual(self.frw.get_names(), name_list)
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.store_names([["1", "2", "3", "4"]])

    def test_get_names(self):
        """
        Test the method to check if players retrieved as list from txt file.

        Test the method to check if error FileNotFound raised.
        """
        names_list = [["a", "0", "0", "0.0"], ["b", "0", "0", "0.0"]]
        self.frw.store_names(names_list)
        self.assertEqual(self.frw.get_names(), names_list)
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.get_names()

    def test_get_name(self):
        """
        Test the method to check if player's info returned as list from txt.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [['a', '0', '0', '0.0']]
        self.frw.store_names(name_list)
        self.assertEqual(self.frw.get_names(), name_list)
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.get_name("abc")

    def test_update_wins(self):
        """
        Test the method to check if player's info uppdated in txt file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [['a', '0', '0', '0.0']]
        self.frw.store_names(name_list)
        self.frw.update_wins("a", 3, 6, 0.0)
        expected_list = [['a', '3', '6', '50.0']]
        self.assertEqual(self.frw.get_names(), expected_list)
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.update_wins("abcd", 4, 5, 2.0)

    def test_store_name(self):
        """
        Test the method to check if player info stored in txt file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [['a', '0', '0', '0.0']]
        self.frw.store_names(name_list)
        expected_list = [['a', '0', '0', '0.0'], ['b', '0', '0', '0.0']]
        self.frw.store_name('b', '0', '0', '0.0')
        self.assertEqual(self.frw.get_names(), expected_list)
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.store_name("abcd", '4', '5', '2.0')

    def test_update_name(self):
        """
        Test the method to check if player's name changed in txt file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [['a', '0', '0', '0.0']]
        self.frw.store_names(name_list)
        expected_list = [['b', '0', '0', '0.0']]
        self.frw.uppdate_name('a', 'b')
        self.assertEqual(self.frw.get_names(), expected_list)
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.uppdate_name("abcd", "efgh")

    def test_get_wins(self):
        """
        Test the method to check if player's wins retrieved from txt file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [['a', '1', '2', '50.0']]
        self.frw.store_names(name_list)
        self.assertEqual(self.frw.get_wins('a'), '1')
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.get_wins("abcd")

    def test_get_times_played(self):
        """
        Test the method to check if times played retrieved from txt file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [['a', '1', '2', '50.0']]
        self.frw.store_names(name_list)
        self.assertEqual(self.frw.get_times_played('a'), '2')
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.get_times_played("abcd")

    def test_get_percentage(self):
        """
        Test the method to check if player's % retrieved from txt file.

        Test the method to check if error FileNotFound raised.
        """
        name_list = [['a', '1', '2', '50.0']]
        self.frw.store_names(name_list)
        self.assertEqual(self.frw.get_percentage('a'), '50.0')
        self.frw.set_file_name("any.txt")
        with self.assertRaises(FileNotFoundError):
            self.frw.get_percentage("abcd")

    def test_set_file_name(self):
        """Test set_file_name method of the FileRW class."""
        self.frw.set_file_name("unknown.txt")
        self.assertEqual(self.frw.get_file_name(), "unknown.txt")

    def test_get_file_name(self):
        """Test get_file_name method of the FileRW class."""
        self.frw.set_file_name("test.txt")
        self.assertEqual(self.frw.get_file_name(), "test.txt")


if __name__ == "__main__":
    unittest.main()
