# Задайте список из n чисел
# последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Enter number: '))


def order_of_numbers(n):
    return [round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)]


print(order_of_numbers(n))
print(round(sum(order_of_numbers(n))))