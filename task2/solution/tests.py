import unittest

from task2.solution.wiki_services import WikiCategoryCounter


class TestWikiCategoryCounter(unittest.TestCase):

    def test_count_category_members(self):
        wiki = WikiCategoryCounter('Категория:Животные_по_алфавиту')
        count_dict = wiki.count_category_members()
        self.assertEqual(len(count_dict), 33)

    def test_count_category_members_all_letters(self):
        wiki = WikiCategoryCounter('Категория:Животные_по_алфавиту', all_letters=True)
        count_dict = wiki.count_category_members()
        self.assertEqual(len(count_dict), 56)


if __name__ == '__main__':
    unittest.main()
