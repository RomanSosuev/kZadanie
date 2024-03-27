#На языке Питон написать программу, которая из файла читает объекты, разделенные  пробелами,
#выводит их на экран, производит заданную обработку и  результат выводит на экран. Обработка:
#через регулярные выражения найти сумму и количество натуральных четных пятиразрядных десятичных чисел,
#в которых третья цифра равна 0, из которых определить максимальное число и количество максимальных чисел.


import re

def find_numbers(text):

    numbers = re.findall(r'\d{1}\d{1}(?:0){1}\d{1}[02468]{1}', text)


    print(numbers)
    numbers = [int(item) for item in numbers]
    count = len(numbers)
    total = sum(numbers)
    maxNumber = max(numbers)
    n = numbers.count(maxNumber)

    return count, total, maxNumber, n

with open('numbers.txt', 'r') as file:
    data = file.read()
print(data)

count, total, maxNumber, n = find_numbers(data)

print("\ncount:", count)
print("total:", total)
print("max ", maxNumber, "Количество максимальных: ", n)
