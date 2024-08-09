import math

# Вариант для ручного ввода
# nums_in = input("Введите числа массива через пробел\n").split()
# nums_out = list(map(int, nums_in))

# Вариант для горизонтального расположения чисел в файле
# with open(input("Укажите файл с данными\n"), 'r', encoding='utf-8') as data_file:
#     bufur = data_file.readlines()[0].split()
#     nums_out = list(map(int, bufur))

# Вариант для вертикального расположения чисел в файле
with open(input("Укажите файл с данными\n"), 'r', encoding='utf-8') as data_file:
    bufur = data_file.readlines()
    nums_out = list(map(int, bufur))



result_digit = math.ceil((max(nums_out))/2)
count = 0
for id, i in enumerate(nums_out):
    while i != result_digit:
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
             i -= 1
             count += 1
        else:
            nums_out[id] = i
print(count)
    