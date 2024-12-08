import unittest

from task3.solution import appearance


class TestAppearance(unittest.TestCase):
    def test_empty_parameters(self):
        self.assertRaises(KeyError, appearance, {})

    def test_all_empty_intervals(self):
        intervals = {'lesson': [],
                     'pupil': [],
                     'tutor': []}
        self.assertRaises(ValueError, appearance, intervals)

    def test_empty_pupil_tutor_intervals(self):
        intervals = {'lesson': [1594663200, 1594666800],
                     'pupil': [],
                     'tutor': []}
        self.assertEqual(appearance(intervals), 0)

    def test_wrong_intervals(self):
        intervals = {'lesson': [1594663200, 1594666800],
                     'pupil': [1594663200, 1594664200, 1594666200],
                     'tutor': []}
        self.assertRaises(ValueError, appearance, intervals)

    def test_non_overlapping_intervals(self):
        intervals = {'lesson': [1594663200, 1594666800],
                     'pupil': [1594663201, 1594664200],
                     'tutor': [1594665201, 1594666200]}
        self.assertEqual(appearance(intervals), 0)

    def test_equal_intervals(self):
        intervals = {'lesson': [1594663200, 1594666800],
                     'pupil': [1594663201, 1594664200],
                     'tutor': [1594663201, 1594664200]}
        self.assertEqual(appearance(intervals), 999)

    def test_overlapping_intervals(self):
        intervals = {'lesson': [1594663200, 1594666800],
                     'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                     'tutor': [1594663290, 1594663430, 1594663443, 1594666473]}
        self.assertEqual(appearance(intervals), 3117)


if __name__ == '__main__':
    unittest.main()