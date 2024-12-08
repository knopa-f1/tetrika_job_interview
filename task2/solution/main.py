from task2.solution.saver_services import save_dict_to_csv
from task2.solution.wiki_services import WikiCategoryCounter

file_name = "beasts.csv"
category_name = 'Категория:Животные_по_алфавиту'


def main():
    wiki = WikiCategoryCounter(category_name)
    counter_dict = wiki.count_category_members()
    save_dict_to_csv(counter_dict, file_name)


if __name__ == '__main__':
    main()