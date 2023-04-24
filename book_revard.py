import csv
import json
from files import CSV_FILE_PATH, JSON_FILE_PATH

lst_users = []
lst_books = []
with open(JSON_FILE_PATH) as f:
    users = json.load(f)
    for q in users:
        users_dict = {}
        users_dict["name"] = f"{q['name']}"
        users_dict["gender"] = f"{q['gender']}"
        users_dict["address"] = f"{q['address']}"
        users_dict["age"] = q['age']
        lst_users.append(users_dict)


with open(CSV_FILE_PATH) as t:
    rd = csv.DictReader(t)
    for row in rd:
        book_dict = {}
        book_dict["Title"] = f"{row['Title']}"
        book_dict['Author'] = f"{row['Author']}"
        book_dict['Pages'] = f"{row['Pages']}"
        book_dict['Genre'] = f"{row['Genre']}"
        lst_books.append(book_dict)


full_round = len(lst_books) // len(lst_users) #число равных кругов распределения
group_books = []
i = 0 #счетчик на формирования пакета книг исходя из формулы количества целовичленного деления кол0ва книг на колво юзеров
p = 0 #переключение раздачи на следующего юзера
n = 0 #всего раздали книг
for t in lst_books: #пока книг меньше 3(целое значение книг на каждого) создаем список книг для юзера
    group_books.append(t)
    i += 1
    n += 1
    if i == full_round and (full_round * len(lst_users) >= n):
        lst_users[p]["books"] = group_books
        i = 0
        p += 1
        group_books = []

p = 0 #распределение остатка книг
if len(lst_books) % len(lst_users) != 0:
    while len(lst_books) >= n:
        lst_users[p]["books"].append(lst_books[n - 1])
        p += 1
        n += 1
print(lst_users)


with open("files/result.json", "w")as f:  #сохранение результата в файл
    s = json.dumps(lst_users, indent=4)
    f.write(s)



