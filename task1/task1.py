import numpy as np


n = int(input("Введите число массива\n"))
m = int(input("Введите интервал\n"))
counter = 1
mass_list = ['1']
b = np.array(list(range(1, n + 1)) * m)
while True:
    g = b[(m-1)*counter]
    if b[(m-1)*counter] != 1:
        mass_list.append(str(b[(m-1)*counter]))
        counter += 1
    else:
        break
print("".join(mass_list))
