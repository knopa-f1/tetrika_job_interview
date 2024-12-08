import os
import unittest

from task2.solution.saver_services import save_dict_to_csv
from task2.solution.wiki_services import WikiCategoryCounter

class TestSaveDictToCsv(unittest.TestCase):
    def test_save_empty_dict(self):
        self.assertRaises(ValueError, save_dict_to_csv, {}, 'test.csv')

    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError, save_dict_to_csv, {"key": "value"}, 'W:\\test.csv')

    def test_access_to_file(self):
        self.assertRaises(PermissionError, save_dict_to_csv, {"key": "value"}, 'C:\\test.csv')

    def test_save_valid_dict(self):
        file_name = 'tempfile.csv'
        save_dict_to_csv({"А": 1, "Б": 2}, 'tempfile.csv')

        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()

        self.assertEqual(content.strip(), "А,1\nБ,2")
        os.remove(file_name)

class TestWikiCategoryCounter(unittest.TestCase):

    def test_count_category_members(self):
        wiki = WikiCategoryCounter('Категория:Животные_по_алфавиту')
        count_dict = wiki.count_category_members()
        self.assertEqual(len(count_dict), 33)

    def test_count_category_members_all_letters(self):
        wiki = WikiCategoryCounter('Категория:Животные_по_алфавиту', all_letters=True)
        count_dict = wiki.count_category_members()
        self.assertEqual(len(count_dict), 56)

    def test_count_category_letter_a(self):
        wiki = WikiCategoryCounter('Категория:Животные_по_алфавиту')
        count_dict = wiki.count_category_members()
        self.assertEqual(count_dict["А"], 1287)

    def test_empty_category(self):
        wiki = WikiCategoryCounter('Категория:Пустая_категория')
        count_dict = wiki.count_category_members()

        self.assertTrue(all(value == 0 for value in count_dict.values()))


if __name__ == '__main__':
    unittest.main()
