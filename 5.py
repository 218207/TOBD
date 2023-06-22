import json
from bs4 import BeautifulSoup
from collections import defaultdict
import pprint

# Считываем данные из XML файла
with open("addres-book-q.xml", "r") as file:
    content = file.read()

soup = BeautifulSoup(content, 'xml')

# Печатаем структуру XML файла
print("Структура XML файла:")
pprint.pprint(content)

# Создаем структуру данных
data_dict = defaultdict(list)

# Ищем все записи в адресной книге
for address in soup.find_all('address'):
    position = address.find("position").get_text()
    name = address.find("name").get_text()
    company = address.find("company").get_text()
    phones = [phone.get_text() for phone in address.find_all('phone')]

    # Создаем словарь для каждого человека
    person_dict = {
        "name": name,
        "company": company,
        "phones": phones,
    }

    # Добавляем человека в список по его должности
    data_dict[position].append(person_dict)

# Сохраняем структуру данных в файл JSON
with open("addres-book-q.json", "w") as file:
    json.dump(data_dict, file, ensure_ascii=False, indent=4)

# Загружаем данные из файла JSON
with open("addres-book-q.json", "r") as file:
    loaded_data = json.load(file)

# Печатаем структуру JSON файла
print("\nСтруктура JSON файла:")
pprint.pprint(loaded_data)

# Проверяем идентичность структур данных
assert data_dict == loaded_data

print("\nСтруктура данных идентична после сохранения и загрузки.")