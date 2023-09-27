# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def select(ar, min, max): 
    out = []
    for i in range(len(ar)):
        v = ar[i]
        if v >= min and v <= max:
            out.append(i)
    return out

def str_to_int_list (str):
    arr = str.split (' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr


ar = str_to_int_list1(input("Задайте список: "))
min = int(input("Введите левую границу диапазона: "))
max = int(input("Введите правую границу диапазона: "))
print(select(ar, min, max))
