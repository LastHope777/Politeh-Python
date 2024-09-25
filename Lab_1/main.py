#Первый номер
a = int(input("Введите число 2024:\n"))
print(a == 2024 or False)

#Второй номер
string = "abc"
answer = input("Попробуйте угадать строку, у вас есть 3 попытки:\n")
print(answer == string or False)
answer = input("Попробуйте угадать строку, у вас есть 2 попытки:\n")
print(answer == string or False)
answer = input("Попробуйте угадать строку, у вас есть 1 попытка:\n")
print(answer == string or False)

#Третий номер
b = 5
print("Привет! Я могу сложить число: ", b)
number = int(input("Введите ваше число:\n"))
print("Результат: ", b + number)

#Четвёртый номер
first_number, second_number = 1, 2
first_answer, second_answer = int(input("Введите первое число:\n")), int(input("Введите второе число:\n"))
print(first_answer ==  first_number and second_answer == second_number and "Оба числа введены верно" or "Хотя бы одно из чисел было указано не верно")

#Пятый номер
symbol = input("Введите один символ:\n")
print("Следующий символ в таблице: ", chr(ord(symbol)+1))

#Шестой номер
number = int(input("Введите число:\n"))
print("Квадрат числа: ", number*number)
print("Квадрат квадрата числа: ", number*number*number*number)

# Седьмой номер
number = float(input("Введите дробное число:\n"))
print(number % 1)
print(number % 10)
