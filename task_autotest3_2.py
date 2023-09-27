# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

# '3 20 50 100' -> [3, 20, 50, 100]
# 10

    
def abs (v):
    if v < 0:
        return -v
    return v      

def str_to_int_list (str):
    arr = str.split (' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return arr
    

list_1 = str_to_int_list(input("Задайте список: "))

k = int(input("Ввдите цифру, которую нужно сравнить с элементами списка: "))

if len(list_1) == 0:
    print('Вы ввели пустой список.')
    exit

min_dist = abs (list_1[0] - k)
min_index = 0
for i in range (len(list_1)):
    v = list_1[i]
    dist = abs (v  - k)
    if dist < min_dist:
        min_dist = dist
        min_index = i
print(list_1[min_index])


    