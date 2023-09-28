# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).

# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


n = (int(input("Введите количество элементов в первом списке: ")))   
m = (int(input("Введите количество элементов во втором списке: ")))

set_1= set()
for i in range(n):
    el_1 = int(input('Введите элемент списка 1: '))
    set_1.add(el_1)

set_2 = set()
for i in range(m):
    el_2 = int(input('Введите элемент списка 2: '))
    set_2.add(el_2)

print(set_1, set_2)

new_set = sorted(set_1 & set_2)

print(new_set)





# from random import randint

# n_set = set(randint(1, 20) for i in range(int(input('Введите количество элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите количество элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(s_set)
