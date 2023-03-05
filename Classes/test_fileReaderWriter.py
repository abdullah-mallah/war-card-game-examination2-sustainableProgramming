from fileReaderWriter import FileRW
import unittest


class Test_fileReaderWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.frw = FileRW('score.txt')

    def test_check_name(self):
        list = [["a", "0", "0", "0.0"]]
        self.frw.store_names(list)
        self.assertEqual(self.frw.check_name("a"), True)
        self.frw._file_name = "any.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.check_name("a")

    def test_store_names(self):
        list = [["a", "0", "0", "0.0"]]
        self.frw.store_names(list)
        self.assertEqual(self.frw.get_names(), list)
        self.frw._file_name = "anyx.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.store_names([["1", "2", "3", "4"]])

    def test_get_names(self):
        list = [["a", "0", "0", "0.0"], ["b", "0", "0", "0.0"]]
        self.frw.store_names(list)
        self.assertEqual(self.frw.get_names(), list)
        self.frw._file_name = "anyb.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.get_names()

    def test_get_name(self):
        list = [['a', '0', '0', '0.0']]
        self.frw.store_names(list)
        self.assertEqual(self.frw.get_names(), list)
        self.frw._file_name = "anyc.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.get_name("abc")

    def test_update_wins(self):
        list = [['a', '0', '0', '0.0']]
        self.frw.store_names(list)
        self.frw.update_wins("a", 3, 6, 0.0)
        expected_list = [['a', '3', '6', '50.0']]
        self.assertEqual(self.frw.get_names(), expected_list)
        self.frw._file_name = "anyd.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.update_wins("abcd", 4, 5, 2.0)

    def test_store_name(self):
        list = [['a', '0', '0', '0.0']]
        self.frw.store_names(list)
        expected_list = [['a', '0', '0', '0.0'], ['b', '0', '0', '0.0']]
        self.frw.store_name('b', '0', '0', '0.0')
        self.assertEqual(self.frw.get_names(), expected_list)
        self.frw._file_name = "anye.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.store_name("abcd", '4', '5', '2.0')

    def test_update_name(self):
        list = [['a', '0', '0', '0.0']]
        self.frw.store_names(list)
        expected_list = [['b', '0', '0', '0.0']]
        self.frw.uppdate_name('a', 'b')
        self.assertEqual(self.frw.get_names(), expected_list)
        self.frw._file_name = "anyf.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.uppdate_name("abcd", "efgh")

    def test_get_wins(self):
        list = [['a', '1', '2', '50.0']]
        self.frw.store_names(list)
        self.assertEqual(self.frw.get_wins('a'), '1')
        self.frw._file_name = "anyg.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.get_wins("abcd")

    def test_get_times_played(self):
        list = [['a', '1', '2', '50.0']]
        self.frw.store_names(list)
        self.assertEqual(self.frw.get_times_played('a'), '2')
        self.frw._file_name = "anyh.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.get_times_played("abcd")

    def test_get_percentage(self):
        list = [['a', '1', '2', '50.0']]
        self.frw.store_names(list)
        self.assertEqual(self.frw.get_percentage('a'), '50.0')
        self.frw._file_name = "anyi.txt"
        with self.assertRaises(FileNotFoundError):
            self.frw.get_percentage("abcd")


if __name__ == "__main__":
    unittest.main()