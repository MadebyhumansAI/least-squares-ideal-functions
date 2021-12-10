import unittest
import pathlib as pl

# Subclass unit test testcase
class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

# Subclassing our own created TestCaseBase class
class DataTest(TestCaseBase):
    def test_test_data(self):
        path = pl.Path("data/test.csv")
        self.assertIsFile(path)

    def test_ideal_data(self):
        path = pl.Path("data/ideal.csv")
        self.assertIsFile(path)

    def test_train_data(self):
        path = pl.Path("data/train.csv")
        self.assertIsFile(path)

if __name__ == '__main__':
    unittest.main()