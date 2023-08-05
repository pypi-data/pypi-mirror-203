# Source: https://docs.python.org/3/library/unittest.html

import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(2 - 1, 1)

    @unittest.skip(reason="This test is expected to fail")
    def test_subtract_failure(self):
        self.assertEqual(2 - 1, 2)


if __name__ == "__main__":
    unittest.main()
