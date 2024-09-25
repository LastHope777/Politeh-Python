import json
import os
from bs4 import BeautifulSoup

def get_user_data():
    full_name = input("Введите ФИО: ")
    age = input("Введите возраст: ")
    favorite_book = input("Введите любимую книгу: ")
    return {"full_name": full_name, "age": age, "favorite_book": favorite_book}

def save_data(data, filename="data.json"):
    if os.path.exists(filename):
        with open(filename, 'r+', encoding='utf-8') as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
            existing_data.append(data)
            file.seek(0)
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([data], file, ensure_ascii=False, indent=4)

user_data = get_user_data()
save_data(user_data)
def read_data(filename="data.json"):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return []
    return []

def display_data(data):
    if not data:
        print("Нет данных.")
        return
    for i, entry in enumerate(data, 1):
        print(f"{i}. {entry}")

def delete_entry(data, index):
    if 0 <= index < len(data):
        del data[index]
    return data

filename = "data.json"
data = read_data(filename)
display_data(data)

if data:
    choice = input("Введите номер строки для удаления (или нажмите Enter, чтобы отменить): ")
    if choice.isdigit():
        index_to_delete = int(choice) - 1
        data = delete_entry(data, index_to_delete)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Строка удалена.")
    else:
        print("Удаление отменено.")
def save_data_html(data, filename="data.html"):
    if os.path.exists(filename):
        with open(filename, 'r+', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            body = soup.body
            if not body:
                body = soup.new_tag('body')
                soup.append(body)
    else:
        soup = BeautifulSoup("<html><body></body></html>", 'html.parser')
        body = soup.body

    entry_tag = soup.new_tag('div')
    entry_tag.string = f"ФИО: {data['full_name']}, Возраст: {data['age']}, Любимая книга: {data['favorite_book']}"
    body.append(entry_tag)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(soup))

user_data = get_user_data()
save_data_html(user_data)