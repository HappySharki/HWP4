# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел: ").split(" ")))
print(lst)
changed_list = []
for i in lst:
    if i not in changed_list:
        changed_list.append(i)
print(changed_list)