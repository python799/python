#4
def sum_numbers():
    n = int(input("Введите количество чисел: "))
    total = 0
    for _ in range(n):
        total += int(input("Введите число: "))
    print("Сумма:", total)


sum_numbers()
