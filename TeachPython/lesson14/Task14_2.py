def sum_digits(n):
    if n < 0:
        return ("Не натуральное!")
    elif n == 0:
        return 0
    else:
        return n%10 + sum_digits(n//10)

try:
    print(sum_digits(int(input())))
except ValueError:
    print("Ошибка")