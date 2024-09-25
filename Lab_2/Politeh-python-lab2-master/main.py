#Первый номер
print(input("Введите первую строку:\n") + input("Введите вторую строку:\n")+ input("Введите третью строку:\n") + input("Введите четвёртую строку:\n"))

#Второй номер
first = int(input("Введите первое число:\n"))
second = int(input("Введите второе число:\n"))
third = int(input("Введите третье число:\n"))
fourth = int(input("Введите четвёртое число:\n"))
fifth = int(input("Введите пятое число:\n"))
print(first, " + ", second, " + ", third, " + ", fourth, " + ", fifth, " = ", first+second+third+fourth+fifth)

#Третий номер
first_name = input("Введите имя первого человека:\n")
first_age = int(input("Введите возраст первого человека:\n"))
second_name = input("Введите имя второго человека:\n")
second_age = int(input("Введите возраст второго человека:\n"))
third_name = input("Введите имя третьего человека:\n")
third_age = int(input("Введите возраст третьего человека:\n"))
print("Информация о людях:\n", first_name.replace(" ", "")," длина имени: ", len(first_name)," возраст: ", first_age , "\n", second_name.replace(" ", ""), " длина имени: ", len(second_name), " возраст: ", second_age, "\n", third_name.replace(" ", ""), " длина имени: ", len(third_name)," возраст: ", third_age)
medium_age = (first_age + second_age + third_age) / 3
formatted = "{:.1f}".format(medium_age).replace('.', ',')
print("Средний возраст",formatted)
print("a" in first_name or "a" in second_name or "a" in third_name or "A" in first_name or "A" in second_name or "A" in third_name)

#Четвёртый номер
number = input("Введите дробное число с запятой в качестве разделителя:\n")

#Первый способ
integer_part, fractional_part = number.split(',')
print("Целая часть:", integer_part, "Дробная часть:", fractional_part)

#Второй способ
integer_part, separator, fractional_part = number.partition(',')
if separator == ',':
    print(f"Целая часть: {integer_part} Дробная часть: {fractional_part}")

#Третий способ
comma_pos = number.index(',')
integer_part = number[:comma_pos]
fractional_part = number[comma_pos + 1:]
print(f"Целая часть: {integer_part} Дробная часть: {fractional_part}")


#Пятый номер
string = input("Введите строку:\n")
print("Python" in string or "питон" in string or "python" in string)