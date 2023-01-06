# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factors(number, d = 2):
    list_1 = []
    while number > 1:
        num1, num2 = divmod(number, d)
        if num2 > 0:
            d += 1
        else: 
            list_1.append(d)
            number = num1
    return list_1

number = int(input())
print(f"{' * '.join(map(str, prime_factors(number)))}")