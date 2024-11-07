# Завдання 1:
# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv
from pathlib import Path

def compare_csv_files(path_to_csv1: Path, path_to_csv2: Path, path_to_output_csv_file: Path):

    with open(path_to_csv1, newline='') as f1, open(path_to_csv2, 'r') as f2:

        reader1 = csv.reader(f1, delimiter=';')
        reader2 = csv.reader(f2)
        diff = []
        equal = []

        for str1, str2 in zip(reader1, reader2):
            if str1 != str2:
                diff.append(str1)
                diff.append(str2)
            else:
                if str1 not in equal:
                    equal.append(str1)

        final_list = equal + diff

    with open(path_to_output_csv_file, 'w+', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(final_list)
        csv_file.close()

file_1 = Path('/home/admin/PycharmProjects/Hillel/pythonProject1/hillel_1609/lesson_13/ideas_for_test/work_with_csv/rmc.csv')
file_2 = Path('/home/admin/PycharmProjects/Hillel/pythonProject1/hillel_1609/lesson_13/ideas_for_test/work_with_csv/r-m-c.csv')
file_result = Path('/home/admin/PycharmProjects/Hillel/pythonProject1/hillel_1609/lesson_13/ideas_for_test/work_with_csv/result.csv')

compare_csv_files(file_1, file_2, file_result)


# Завдання 2:
# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json. результат для невалідного файлу виведіть
# через логер на рівні еррор у файл json__<your_second_name>.log


from pathlib import Path
import json
import logging

path = Path('/home/admin/PycharmProjects/Hillel/pythonProject1/hillel_1609/lesson_13/ideas_for_test/work_with_json/')
files = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
file_handler = logging.FileHandler(path / 'json_Kobernik.log')
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

for file in files:
    with open(path / file, 'r', encoding='utf-8') as q:
        try:
            data = json.load(q)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error in {file}: {e}")


# Завдання 3:
## Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення значення timingExbytes/incoming
# результат виведіть у консоль через логер на рівні інфо

import logging
import xml.etree.ElementTree as et

# Завантаження XML-файлу
def find_xml_papameter(group_number: int):

    tree = et.parse('/home/admin/PycharmProjects/Hillel/pythonProject1/hillel_1609/lesson_13/ideas_for_test/work_with_xml/groups.xml')
    root = tree.getroot()
    checked = False
    # Пошук елементу timing_exbytes/incoming у для заданої групи
    for group in root.findall('group'):
        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None and group.find('number').text == f'{group_number}':
                if group.find('number').text == f'{group_number}':
                    log_message = f"Group/number: {group_number}, timing_exbytes/incoming: {incoming.text}"
                    checked = True


    # Створення та налаштування логера
    logging.basicConfig(
        level=logging.INFO,
        force=True
    )
    console_handler = logging.StreamHandler()
    logging.getLogger('').addHandler(console_handler)
    if checked:
        logging.info(log_message)
    else:
        print(f'Group/number \'{group_number}\' not found!')

find_xml_papameter(8)
