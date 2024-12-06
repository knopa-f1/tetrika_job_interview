import unittest

from task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_three(a: int, b: int, c: float) -> float:
    return a + b + c


@strict
def sum_two_without_ann(a, b):
    return a + b


class TestStrict(unittest.TestCase):

    def test_correct_args(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_incorrect_args_float(self):
        self.assertRaises(TypeError, sum_two, (1, 2.3))

    def test_incorrect_args_bool(self):
        self.assertRaises(TypeError, sum_two, (1, False))

    def test_correct_args_kwargs(self):
        self.assertEqual(sum_two(3, b=2), 5)

    def test_correct_kwargs(self):
        self.assertEqual(sum_two(b=3, a=2), 5)

    def test_incorrect_kwargs_bool(self):
        self.assertRaises(TypeError, sum_two, b=True, a=7)

    def test_sum_without_ann(self):
        self.assertRaises(TypeError, sum_two_without_ann, (1, 2))


if __name__ == '__main__':
    unittest.main()
