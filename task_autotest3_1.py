# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1
# (int(input("Задайте список: ")))

list_1 = (str(input("Задайте список: ")))
k = (str(input("Ввдите цифру, которую нужно найти в списке: ")))

count = 0

for i in range (len(list_1)):
    if list_1[i] == k: 
        count += 1
print (count)


# эталонное решение

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)