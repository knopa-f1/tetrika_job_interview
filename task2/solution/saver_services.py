import csv


def save_dict_to_csv(saving_dict: dict, file_name: str) -> None:
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(saving_dict.items())