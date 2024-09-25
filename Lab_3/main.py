#Первый номер
# создание множеств
s1 = set() # пустое обычное множество set(iteareble)
s2 = {1, 2, 4, 4, 4, 'qwe'}
d = {} # d не будет являться множеством
fs = frozenset() # замороженное множество
# перебор элементов
print("Значения, которые содержатся в s2:")
for i in s2:
 print(i)
# фильтрация значений списка на уникальность
l1 = [1, 2, 4, 63, 4, 2, 12, 1, 2, 32, 12, 32]
l2 = list(set(l1))
print("Значения, которые содержатся в l1:")
print(l2)
s1 = set([1, 2, 5, 3, '1'])
print("Содержится ли 3 в s1:")
print(3 in s1)
s1 = set([1, 2, 5, 3, '1'])
s2 = {1, 2, 4, 4, 4, 'qwe'}
print("Добавили 6 в s1:")
s1.add(6)
print(s1)
# удаление
s1.remove(1) # если элемента нет, то будет вызвана ошибка
print("Удалили 1 из s1")
print(s1)
s1.discard(1) # если элемента нет, то ничего не произойдет
val = s1.pop() # удаляет и возвращает случайный* элемент
print("Достали первое значение:")
print(s1)
# сложение (объединение)
s3 = s1 | s2
print("Объединили s1 и s2:")
print(s3)
s3 = s1.union(s2) # или s2.union(s1)
# разница (порядок переменных имеет значение)

# ищем элементы из s1, которых нет в s2
s3 = s1 - s2
print("Элементы из s1, которых нет в s2:")
print(s3)
s3 = s1.difference(s2)
# симметричная разница (нет в обоих множествах)
s3 = s1 ^ s2
print("Симметрическая разница:")
print(s3)
# перечисление (общие элементы)
s4 = s1 & s2
print("Общие элементы:")
print(s4)

#Второй номер
map = []
a = 7
for i in range(a):
    map.append([0] * a)
print("   А  Б  В  Г  Д  Е  Ё")
for i in range(a):
    print(i + 1,map[i])
ships = ["А6", "В2", "Г3"]
count = input("Сколько выстрелов хотите сделать?\n")
for i in range(int(count)):
 choose = input("Введите координаты в формате: А1\n")
 if (choose in ships):
  print("Попал")
 else:
  print("Мимо")

#Мины
n = 3
arr = []
for x in range(n):
    arr.append([])
    for y in range(n):
        arr[x].append([])
        for z in range(n):
            arr[x][y].append(0)
for i in range(n):
 print(arr[i])
bombs = ["123", "333", "231"]
count = int(input("Введите количество попыток:\n"))
for i in range(count):
 choose = input("Введите координаты в формате: 000 (строка колонка номер в колонке (Начинается всё с 1):\n")
 if choose in bombs:
  print("Подрыв")
 else:
  print("Мимо")

#Третий номер
string = input("Введите предложение:\n")
print("Зашифрованное предложение:")
for i in range(len(string)):
    if ord(string[i]) == 1071:
        print("А", end="")
    elif ord(string[i]) == 1103:
        print("а", end="")
    else:
        print(chr(ord(string[i]) + 1), end = "")

#Четвёртый номер
print("\nРасшифрованное предложение:")
for i in range(len(string)):
    print(chr(ord(string[i])), end = "")
#Если записывать в отдельную переменную, то просто надо вычесть 1


#Пятый номер
dictionary = set()
a = True
while a == True:
    word = input("Введите слово:\n")
    if word not in dictionary:
        print("Слово добавлено во множество")
        dictionary.add(word)
    else:
        print("Это слово уже есть во множестве")
        a = False

#Шестой номер
user_credentials = {
    "Самый слабый человек в мире": "Позор"
}
a = True
while a == True:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login in user_credentials and user_credentials[login] == password:
        print(f"Доступ разрешен для пользователя: {login}")
        a = False
    else:
        print("Неверный логин или пароль")


#Седьмой номер
initial_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 4, 9]
unique_values_dict = {}
unique_values_set = set()

for index, value in enumerate(initial_list):
    if value not in unique_values_set:
        unique_values_set.add(value)
        unique_values_dict[index + 3] = value
print(unique_values_dict)

#Восьмой номер
def calculate(expression):
    tokens = expression.split()
    result = float(tokens[0])
    index = 1
    while index < len(tokens):
        operator = tokens[index]
        next_number = float(tokens[index + 1])

        if operator == '+':
            result += next_number
        elif operator == '-':
            result -= next_number
        elif operator == '*':
            result *= next_number
        elif operator == '/':
            if next_number != 0:
                result /= next_number
            else:
                return "Ошибка: деление на ноль"
        index += 2
    return result


expression = input("Введите выражение (например, '2 + 3 * 4 / 2 - 1'): ")
result = calculate(expression)
print(f"Результат: {result}")