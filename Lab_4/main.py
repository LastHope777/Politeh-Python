#Первый номер
def square(number):
    return number ** 2
numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))

numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

out_filter = filter(filter_odd_num, numbers)
print("Отфильтрованный список: ", list(out_filter))

vowels = [9, 6, 2, 1, 7]
vowels.sort()
print('Отсортированный массив:', vowels)


#Второй номер
arr = [0]*10
for i in range(len(arr)):
    arr[i] = int(input(f"Введите {i+1} элемент:\n"))
print(arr)


#Третий номер
def custom_sort(numbers):
    return sorted(numbers, key=lambda x: x)

numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = custom_sort(numbers)
print(f"Отсортированные числа: {sorted_numbers}")


#Четвёртый номер
def custom_filter(numbers, criterion):
    return list(filter(criterion, numbers))

# Пример использования с разными критериями
numbers = [5, 2, 9, 1, 5, 6]

# 1. Четные числа
even_numbers = custom_filter(numbers, lambda x: x % 2 == 0)
print(f"Четные числа: {even_numbers}")

# 2. Нечетные числа
odd_numbers = custom_filter(numbers, lambda x: x % 2 != 0)
print(f"Нечетные числа: {odd_numbers}")

# 3. Числа больше 5
greater_than_five = custom_filter(numbers, lambda x: x > 5)
print(f"Числа больше 5: {greater_than_five}")

# 4. Числа меньше 5
less_than_five = custom_filter(numbers, lambda x: x < 5)
print(f"Числа меньше 5: {less_than_five}")

# 5. Числа, кратные 3
divisible_by_three = custom_filter(numbers, lambda x: x % 3 == 0)
print(f"Числа, кратные 3: {divisible_by_three}")

#Пятый номер
def get_user_matrix():
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            value = int(input(f"Введите значение для [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix

def transform_matrix(matrix):
    new_matrix = []
    for i, row in enumerate(matrix):
        if i % 2 == 0:
            new_matrix.append(sorted(row))
        else:
            new_matrix.append(sorted(row, reverse=True))
    return new_matrix

matrix = get_user_matrix()
print(f"Исходный массив: {matrix}")

transformed_matrix = transform_matrix(matrix)
print(f"Преобразованный массив: {transformed_matrix}")


#Шестой номер
def password_protected(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password == "your_password":
            # Первый номер
            def square(number):
                return number ** 2

            numbers = [1, 2, 3, 4, 5]
            squared = map(square, numbers)
            print(list(squared))

            numbers = [1, 2, 4, 5, 7, 8, 10, 11]

            def filter_odd_num(in_num):
                if (in_num % 2) == 0:
                    return True
                else:
                    return False

            out_filter = filter(filter_odd_num, numbers)
            print("Отфильтрованный список: ", list(out_filter))

            vowels = [9, 6, 2, 1, 7]
            vowels.sort()
            print('Отсортированный массив:', vowels)

        else:
            print("Неправильный пароль.")
    return wrapper


def example_function():
    print("Выполненная функция!")