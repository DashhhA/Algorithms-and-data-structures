import unittest
from check_brackets.main import check_brackets


class check_brackets_tests(unittest.TestCase):
    def test_0(self):
        expected = "Success"
        actual = check_brackets("")
        self.assertEqual(expected, actual)

    def test_1(self):
        expected = "Success"
        actual = check_brackets("{}[]")
        self.assertEqual(expected, actual)

    def test_2(self):
        expected = "Success"
        actual = check_brackets("()")
        self.assertEqual(expected, actual)

    def test_3(self):
        expected = "Success"
        actual = check_brackets("[()]")
        self.assertEqual(expected, actual)

    def test_4(self):
        expected = "Success"
        actual = check_brackets("(())")
        self.assertEqual(expected, actual)

    def test_5(self):
        expected = "Success"
        actual = check_brackets("{[]}()")
        self.assertEqual(expected, actual)

    def test_6(self):
        expected = 1
        actual = check_brackets("{")
        self.assertEqual(expected, actual)

    def test_7(self):
        expected = 3
        actual = check_brackets("{[}")
        self.assertEqual(expected, actual)

    def test_8(self):
        expected = 10
        actual = check_brackets("foo(bar[i);")
        self.assertEqual(expected, actual)

    def test_9(self):
        expected = "Success"
        actual = check_brackets("foo(bar);")
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()