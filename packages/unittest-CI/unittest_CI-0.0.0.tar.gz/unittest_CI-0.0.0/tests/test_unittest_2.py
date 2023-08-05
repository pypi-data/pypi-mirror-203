import unittest


class TestTrivial(unittest.TestCase):
    def test_trivial(self):
        self.assertTrue(True)

    @unittest.skip(reason="This test is expected to fail")
    def test_failure(self):
        self.assertTrue(False)
