# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



def fill_array(a1, d, n):
    list = [a1]
    for i in range(1, n):
        list.append(a1 + d * i)
       
    return list


a1 = int(input("Введите первый элемент массива: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов в массиве: "))
print(fill_array(a1, d, n))





